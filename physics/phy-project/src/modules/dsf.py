# Code for the Dynamic Structure factor

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 

import van_hove

def dynamic_structure_factor(set_of_frames):
    time_slots = list(range(1, 20, 5))
    print("Working Van Hove to be used for DSF", time_slots)

    dict_for_plot, time_slot_sizes = van_hove.van_hove_corr(set_of_frames,time_slots, "dsf_van_hove.png")
    print("van hove has returned")
    dist_range = 30 # in A
    dynamic_structure_matrix = np.zeros((len(time_slot_sizes), dist_range))

    for i, time_slot in enumerate(time_slots):
        for dist in range(1, dist_range):
            # so, we have the time and distance
            relevant_dict = dict_for_plot[time_slot]
            # now we have to calculate for ever distance that we have
            if relevant_dict.get(dist):
                # then it exists, good
                dynamic_structure_matrix[i][dist] = relevant_dict[dist]/time_slot_sizes[time_slot]

            else:
                dynamic_structure_matrix[i][dist] = 0
    # this is my matrix

    # now we have to perform FFT's

    distance_based_fourier = np.array( [np.fft.fft(row) for row in dynamic_structure_matrix] ).T

    time_based_fourier = (np.array( [np.absolute(np.fft.fft(row)) for row in distance_based_fourier] ))

    colors = cm.rainbow(np.linspace(0, 1, len(time_based_fourier)))

    for i,row in enumerate(time_based_fourier):
        # print(i)
        plt.plot(row, c=colors[i])

    plt.savefig("graphs/dsf_main.png")
    plt.title("Dynamic Structure Factor")
    plt.show()
    print("Dynamic Structure Factor has ended")

    return