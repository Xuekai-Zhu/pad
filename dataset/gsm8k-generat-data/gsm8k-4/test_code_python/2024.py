def solution():
    """At a birthday party, there are 20 red balloons and 15 green balloons. Before the party started, 3 red and 2 green balloons burst. How many balloons are left?"""
    # Define the initial number of red and green balloons
    red_balloons = 20
    green_balloons = 15

    # Subtract the burst balloons from the initial count
    red_balloons -= 3
    green_balloons -= 2

    # Calculate the total number of balloons left
    total_balloons = red_balloons + green_balloons

    # return the result
    result = total_balloons
    return result

print(solution())