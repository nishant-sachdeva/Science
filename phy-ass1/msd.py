import matplotlib.pyplot as plt
import numpy as np

def get_dist(arr1, arr2):
	# get squared distance between 2 2d arrays
	return np.sum(np.square(arr1 - arr2))

def mean_displacement(set_of_frames):
	# we have the set of frames. We calculate msd, make the graph, and calculate the diffusion coefficient
	print(np.shape(set_of_frames))
	atoms, frames, coords = np.shape(set_of_frames)
	
	distance_values = {}

	for frame1 in range(frames):
		for frame2 in range(frame1+1, frames):
			plate1 = set_of_frames[:, frame1, :]
			plate2 = set_of_frames[:, frame2, :]

			plate1 = plate1[::3, :]
			plate2 = plate2[::3, :]

			time_slot = frame2 - frame1
			distance = get_dist(plate2 , plate1)
			
			if not distance_values.get(time_slot):
				distance_values[time_slot] = [atoms, distance]
			else:
				distance_values[time_slot][0] += atoms
				distance_values[time_slot][1] += distance
	
	# now we have the sums and the numbers. We should plot the values

	

	plot_list  = [ (distance_values[key][1] / distance_values[key][0]) for key in distance_values]

	diffusion_coefficient = (plot_list[249] - plot_list[200])/300
	print("Diffusion coefficient is " , diffusion_coefficient)

	plt.plot(plot_list)
	plt.show()

	return
	# we have calculated the 
