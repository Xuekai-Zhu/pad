def solution():
    # Define Sam's widget production rate
    sam_rate = 1/10  # widgets per minute

    # Define Jack and Tony's combined widget production rate
    jack_tony_rate = 2/15  # widgets per minute

    # Define Sam's and Jack's working times in minutes
    sam_time = 6 * 60  # minutes
    jack_time = 4 * 60  # minutes

    # Define Tony's working time in minutes
    tony_time = 8 * 60  # minutes

    # Calculate the total number of widgets produced
    total_widgets = 68

    # Calculate the number of widgets produced by Sam and Jack
    sam_jack_widgets = sam_rate * sam_time + jack_tony_rate * jack_time

    # Calculate the number of widgets produced by Tony
    tony_widgets = total_widgets - sam_jack_widgets

    # Calculate Tony's widget production rate
    tony_rate = tony_widgets / tony_time

    # Convert Tony's widget production rate to minutes per widget
    tony_time_per_widget = 1 / tony_rate * 60

    result = tony_time_per_widget
    return result

print(solution())