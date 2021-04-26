import numpy as np
from config import generate_initial_config
from config import generate_next_frame
from config import get_optimal_coordinates
from config import plot_rij

import msd
import van_hove
import vel_corr
import dsf

import constants

N = constants.N

lx, ly , lz = constants.lx, constants.ly, constants.lz 

min_dist = constants.min_dist

epsilon = constants.epsilon # KCal/Mole

number_of_frames = constants.number_of_frames

print("going to generate the initial config array")


initial_frame = generate_initial_config(lx, ly, lz, N, min_dist)

print("the initial config array is \n", initial_frame)

rows, cols = np.shape(initial_frame)


plot_rij(initial_frame)

current_frame = get_optimal_coordinates(initial_frame)

print(current_frame)


velocities = []
forces = []
set_of_frames = []

for i in range(number_of_frames):
	print(str(i) + " th frame is being generated")

	next_frame, velocities, mass = generate_next_frame(current_frame, velocities, forces)

	set_of_frames.append(next_frame)

	current_frame = next_frame


set_of_frames = np.stack(set_of_frames, axis=1)


atoms, frames, coords = np.shape(set_of_frames)
	# data has been read
print("We have " + str(atoms) + " atoms per frame. and " + str(frames) + " frames in total " )

# print("Operations are as follows :\n 1. MSD and diffusion coefficient \n 2. Van Hove Correlation Function \n 3. Velocity Correlation Function \n 4. Total Dipole Dipole Correlation Function")

msd.mean_displacement(set_of_frames)

van_hove.van_hove_corr(set_of_frames)

vel_corr.vel_corr_func(set_of_frames)

dsf.dynamic_structure_factor(set_of_frames)

print("Functions executed. Program ended")

