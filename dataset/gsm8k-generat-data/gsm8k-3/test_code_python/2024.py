def solution():
    """At a birthday party, there are 20 red balloons and 15 green balloons. Before the party started, 3 red and 2 green balloons burst. How many balloons are left?"""
    # Define the initial number of red and green balloons
    RED_BALLOONS = 20
    GREEN_BALLOONS = 15

    # Define the number of red and green balloons that burst
    RED_BURST = 3
    GREEN_BURST = 2

    # Calculate the number of remaining red and green balloons
    remaining_red = RED_BALLOONS - RED_BURST
    remaining_green = GREEN_BALLOONS - GREEN_BURST

    # Calculate the total number of remaining balloons
    total_remaining = remaining_red + remaining_green

    # Display the total number of remaining balloons
    result = total_remaining
    return result

print(solution())