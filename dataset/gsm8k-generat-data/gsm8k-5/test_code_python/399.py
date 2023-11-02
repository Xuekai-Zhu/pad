def solution():
    # Calculate the total time Sam worked in minutes
    sam_time = 6 * 60  # Sam worked for 6 hours

    # Calculate the total time Jack worked in minutes
    jack_time = 4 * 60  # Jack worked for 4 hours

    # Calculate the total time Tony worked in minutes
    tony_time = 8 * 60  # Tony worked for 8 hours

    # Calculate the total number of widgets Sam and Jack assembled together
    sam_jack_widgets = (sam_time // 10 + jack_time // 15 * 2)

    # Calculate the number of widgets Tony assembled
    tony_widgets = 68 - sam_jack_widgets

    # Calculate the time it took Tony to assemble one widget in minutes
    tony_time_per_widget = tony_time / tony_widgets

    result = tony_time_per_widget
    return result

print(solution())