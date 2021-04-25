import numpy as np 
import matplotlib.pyplot as plt 

def get_dipole(set_of_frames):

	# for every frame
		# for every oxygen atom
	print(np.shape(set_of_frames))
	atoms, frames, coords = np.shape(set_of_frames)
	
	dipole = np.zeros((frames, 3))

	for frame in range(frames):
		plate1 = set_of_frames[:, frame, :][::3, :]
		plate2 = set_of_frames[:, frame, :][1::3, :]
		plate3 = set_of_frames[:, frame, :][2::3, :]

		dipole[frame] = np.sum((2*plate1 - plate2 - plate3), axis = 0)


	dipole_values = {}
	for frame1 in range(frames):
		for frame2 in range(frame1, frames):
			time_slot = frame2 - frame1

			if not dipole_values.get(time_slot):
				dipole_values[time_slot] = [0,0]

			dip_corr = np.sum(np.multiply(dipole[frame1] , dipole[frame2] ))

			dipole_values[time_slot][0] += dip_corr
			dipole_values[time_slot][1] += 1



	dipole_list = [dipole_values[key][0] / dipole_values[key][1] for key in dipole_values]

	plt.plot(dipole_list)
	plt.show()


	return