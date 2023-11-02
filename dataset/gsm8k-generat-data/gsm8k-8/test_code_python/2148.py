def solution():
    # Calculate the total time Missy spends watching reality shows
    reality_show_time = 5 * 28

    # Add the time spent watching the cartoon
    total_time = reality_show_time + 10

    # Convert the total time to hours and minutes
    hours = int(total_time / 60)
    minutes = total_time % 60

    # Format the output as "X hours and Y minutes"
    output = "{} hours and {} minutes".format(hours, minutes)
    return output

print(solution())