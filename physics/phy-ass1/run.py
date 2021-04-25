import numpy as np

import msd
import van_hove
import vel_corr
import dipole



def main():

	# read file path as input
	file_path = input("please enter file path : ")
	try:
		f = open(file_path, 'r')
	except:
		print("Could not read file. Try again. Exiting now")
		return
	# we are here, it means, we read the file
	set_of_frames = []
	frame_array = []

	while True:
		line = f.readline().strip().split()

		if not line:
			break
		elif line[0] == "ATOM":
			# we'll make an atom
			atom_array = np.asarray([float(line[5]) , float(line[6]) , float(line[7])])
			frame_array.append(atom_array)

		elif line[0] == "END":
			# we'll make a new numpy array to be appended
			set_of_frames.append(np.asarray(frame_array))
			frame_array = []
			# print(frame_array)
		else:
			continue

	f.close()

	set_of_frames = np.stack(set_of_frames, axis=1)

	atoms, frames, coords = np.shape(set_of_frames)
	# data has been read
	print("We have " + str(atoms) + " atoms per frame. and " + str(frames) + " frames in total " )

	print("Operations are as follows :\n 1. MSD and diffusion coefficient \n 2. Van Hove Correlation Function \n 3. Velocity Correlation Function \n 4. Total Dipole Dipole Correlation Function")

	while True:
		function = int(input("Enter number for the function you want => "))

		if(function == 1):
			msd.mean_displacement(set_of_frames)
		elif(function == 2):
			van_hove.van_hove_corr(set_of_frames)
		elif(function == 3):
			vel_corr.vel_corr_func(set_of_frames)
		elif(function == 4):
			dipole.get_dipole(set_of_frames)
		else:
			print("no relevant function found")

		cont = int(input("Do you wanna continue (1-yes/0-no) => ") )
		if(cont == 1):
			continue
		else:
			break


	print("Functions executed. Program ended")


if __name__ =='__main__':
	main()