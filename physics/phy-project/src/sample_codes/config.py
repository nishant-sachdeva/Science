import numpy as np
import random
import constants

from scipy import stats

def get_distance(pointA, pointB):
    dist = np.linalg.norm(pointA - pointB)

    return dist


def check_dist_greater_than_min(min_dist , points_array, pointA):
    for point in points_array:
        dist = get_distance(point, pointA)

        if dist < min_dist:
            return False

    return True


def generate_initial_config(lx, ly, lz, N, min_dist):
    # we have to generate initial position arrays for all the given atoms
    # lx, ly, lz are the box dimensions
    points_array = []

    for i in range(N):
        # we have to make N points
        dist_condition_satisfied = False

        while dist_condition_satisfied == False:
            a = [ random.uniform(0, lx), random.uniform(0,ly), random.uniform(0, lz) ]

            dist_condition_satisfied = check_dist_greater_than_min(min_dist, points_array, a)

        points_array.append(np.asarray(a))

    return np.asarray(points_array)


def total_potential_energy(set_of_coordinates, epsilon=0.238, sigma=3.4):
    # take every coordinate and calculate the total potential energy
    total_potential_energy = 0.0
    for i,coord1 in enumerate(set_of_coordinates):
        for j, coord2 in enumerate(set_of_coordinates):
            if j <= i:
                continue
            else:
                temp_dist = float(get_distance(coord1, coord2))

                temp = 4 * epsilon * ( ((sigma/temp_dist)** 12)- ((sigma/temp_dist)**6))
                total_potential_energy += temp


    return total_potential_energy

def force_on(coord, set_of_coordinates, epsilon = 0.238, sigma = 3.4):
    # here, we calculate the force on a coordinate by all other coordinates
    total_force = [0.0,0.0,0.0]
    for point in set_of_coordinates:
        if np.isclose(point, coord).all():
            continue

        direction = (coord - point)/np.linalg.norm(coord-point)

        temp_dist = float(get_distance(point, coord))

        magnitude = 4*epsilon* ( ( ((sigma/temp_dist)**12)* (-12.0/temp_dist) ) -  ( ((sigma/temp_dist)**6)*(-6.0/temp_dist)))

        force_value = magnitude * direction

        total_force += force_value

    return total_force


def boundary_condition_check(point):
    x = point[0]
    y = point[1]
    z = point[2]

    if x > constants.lx:
        x = constants.lx
    elif x < 0:
        x = 0

    if y > constants.ly:
        y = constants.ly
    elif y < 0:
        y = 0

    if z > constants.lz:
        z = constants.lz
    elif z < 0 :
        z = 0

    point = [x,y,z]

    return point

def perform_gradient_descent(set_of_coordinates , learning_rate = 0.1):

    for i, coord in enumerate(set_of_coordinates):

        set_of_coordinates[i] = coord - learning_rate * force_on(coord, set_of_coordinates)

        set_of_coordinates[i] = boundary_condition_check(set_of_coordinates[i])

    return np.asarray(set_of_coordinates)

def get_optimal_coordinates(set_of_coordinates, epsilon=0.238, sigma=3.4):
    # using gradient descent, find the coordinates that will give the minimum energy
    current_energy = total_potential_energy(set_of_coordinates)
    print("Current energy is ", current_energy)
    # looks like this is arbitrarily chosen
    iterations = 0
    while True:
        iterations += 1
        print(iterations ,  current_energy)
        new_coordinates = perform_gradient_descent(set_of_coordinates)

        new_energy = total_potential_energy(new_coordinates)

        if np.isclose(new_energy, current_energy, atol=0.01) :
            # then we have converged
            print("the optimal potential energy is ", new_energy)
            break

        set_of_coordinates = new_coordinates
        current_energy = new_energy

    print("iterations are " , iterations)
    return new_coordinates

def generate_maxwell_velocities(number_of_velocities):
    velocities = []
    magnitudes = stats.maxwell.rvs(number_of_velocities, size=constants.N)

    for i in range(number_of_velocities):
        direction = np.asarray([ random.random(), random.random(), random.random()])

        # velocities cannot be 0, hence we keep shifting it around,
        while np.isclose(direction , np.asarray([0,0,0]) ).all() :
            direction = np.asarray([ random.random(), random.random(), random.random()])

        direction = direction / np.linalg.norm(direction)

        vel = direction * magnitudes[i]
        velocities.append(vel)


    return np.asarray(velocities)

def generate_next_frame(current_frame, velocities = [], forces = [], timestep = float(constants.timestep)):

    if velocities == []:
        # generate a set of 0s for initial velocities
        velocities = generate_maxwell_velocities(constants.N)

    if forces == []:
        # get the set of forces for initial forces

        for coord in current_frame:
            force = force_on(coord, current_frame)
            forces.append(force)

        forces = np.asarray(forces)


    next_frame = []
    for i, point in enumerate(current_frame):
        new_point = point + velocities[i]*timestep + forces[i] * (timestep**2)/2.0
        
        new_point = boundary_condition_check(new_point)

        next_frame.append(new_point)
    next_frame = np.asarray(next_frame, dtype='float64')


    # getting new forces using the new coordinates
    new_forces = []

    for coord in next_frame:
        new_force = force_on(coord, next_frame)
        new_forces.append(new_force)
    
    new_velocities = []
    for i, point in enumerate(velocities):
        new_velocity = velocities[i] + (forces[i] + new_forces[i])*timestep*0.5
        new_velocities.append(new_velocity)
        
    

    return next_frame, new_velocities, new_forces