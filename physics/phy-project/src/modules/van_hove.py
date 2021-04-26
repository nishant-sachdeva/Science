import numpy as np 
import matplotlib.pyplot as plt 

def get_dist(arr1, arr2):
	# get squared distance between 2 2d arrays

	# return np.sqrt(np.sum(np.square(arr1 - arr2)))
    return np.linalg.norm(arr1 - arr2)

def van_hove_corr(set_of_frames, plot_for_slots=[10], name="van_hove.png"):
    # van hove correlation has to be calculated
    # first, we have to get %3 == 0 rows, ( cuz they are oxygen atoms)
    mean_values_list = {}

    for item in plot_for_slots:
        mean_values_list[item] = {}

    # so we have a dict for every time slot

    print("plotting correlation for time differences ", plot_for_slots)

    print(np.shape(set_of_frames))
    atoms, frames, coords = np.shape(set_of_frames)

    distance_values = {}
    time_slot_sizes = {}

    for frame1 in range(frames):
        for time_slot in plot_for_slots:
            frame2 = frame1 + time_slot

            if frame2 >= frames:
                break

            # print(frame1, "working on ", frame2)

            if not time_slot_sizes.get(time_slot):
                time_slot_sizes[time_slot] = 0

            # now, we know that we are only looking for plottable values

            plate1 = set_of_frames[:, frame1, :]
            plate2 = set_of_frames[:, frame2, :]

            time_slot_sizes[time_slot] += np.size(plate1)**2

            for atom1 in plate1:
                for atom2 in plate2:
                    dist = round(get_dist(atom1, atom2)*1e10)
                    if not mean_values_list[time_slot].get(dist):
                        mean_values_list[time_slot][dist] = 0

                    mean_values_list[time_slot][dist] += 1


    # now we start plotting, 
    dict_for_plot = {}

    for time_slot in plot_for_slots:
        dict_for_plot[time_slot] = {key:mean_values_list[time_slot][key] for key in sorted(mean_values_list[time_slot].keys()) }


    print("Basic dicts made")

    for time_slot in plot_for_slots:
    	relevant_dict = dict_for_plot[time_slot]
    	print("working on time slot " , time_slot)
    	x_arr = list(relevant_dict.keys())
    	y_arr = [ relevant_dict[key]/time_slot_sizes[time_slot] for key in relevant_dict ]		 

    	plt.plot(y_arr)
    	# plt.show()
    graph_name = "graphs/" + name
    plt.title("Van Hove")
    plt.savefig(graph_name)
    plt.show()

    print("Van Hove is done")


    return dict_for_plot, time_slot_sizes 