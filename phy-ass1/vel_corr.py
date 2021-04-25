import numpy as np 
import matplotlib.pyplot as plt 

def vel_corr_func(set_of_frames):

	# first find velocities, lolz

	print(np.shape(set_of_frames))
	atoms, frames, coords = np.shape(set_of_frames)
	velocities = np.zeros(np.shape(set_of_frames))

	for i in range(frames-1):
		frame1 = set_of_frames[:, i, :]
		frame2 = set_of_frames[:, i+1, :]

		velocities[:, i, :] = np.copy(frame2 - frame1)

	# this gives us velocities of particles at all times [o, t-1]
	
	corr_values = {}

	for frame1 in range(frames):
		for frame2 in range(frame1, frames):
			if(velocities[:, frame2, :][0][0] == -1.0):
				continue

			time_slot = frame2 - frame1

			if not corr_values.get(time_slot):
				corr_values[time_slot] = [0,0]

			plate1 = velocities[:, frame1, :]
			plate2 = velocities[:, frame2, :]

			# so , here we have two plates. We need to pick rows%3 == 0
			plate1 = plate1[::3, :]
			plate2 = plate2[::3, :]

			vel_correlation = np.sum(np.multiply(plate1, plate2))

			corr_values[time_slot][0] += vel_correlation
			corr_values[time_slot][1] += np.shape(plate1)[0]


	correlation_list = [corr_values[k][0] / corr_values[k][1] for k in corr_values]
	
	plt.plot(correlation_list)
	plt.show()	

	return