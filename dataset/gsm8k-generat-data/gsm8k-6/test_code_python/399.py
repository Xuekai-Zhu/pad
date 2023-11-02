def solution():
    # Calculate the total time worked by Sam and Jack combined
    sam_time = 6 * 60  # Sam worked for 6 hours
    jack_time = 4 * 60  # Jack helped for 4 hours
    sam_jack_time = sam_time + jack_time  # total time worked by Sam and Jack
    sam_jack_widgets = 2 * (sam_jack_time // 15)  # total number of widgets assembled by Sam and Jack

    # Calculate the total time worked by Tony
    tony_time = 8 * 60  # Tony worked for 8 hours
    tony_widgets = 68 - sam_jack_widgets  # total number of widgets assembled by Tony alone

    # Calculate the time taken by Tony to assemble one widget
    time_per_widget = tony_time / tony_widgets
    result = time_per_widget
    return result

print(solution())