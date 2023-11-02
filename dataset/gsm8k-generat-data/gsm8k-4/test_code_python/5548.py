def solution():
    """Kira's cat eats a pound of kibble every 4 hours. Kira fills her cat's bowl with 3 pounds of kibble before going to work. When she returns, Kira weighs the bowl and there is still 1 pound left. How many hours was Kira away from home?"""
    # Define the initial amount of kibble in the bowl
    initial_kibble = 3

    # Define the amount of kibble remaining in the bowl when Kira returns
    remaining_kibble = 1

    # Calculate the amount of kibble the cat has eaten
    eaten_kibble = initial_kibble - remaining_kibble

    # Calculate the number of 4-hour intervals that have passed
    intervals = eaten_kibble / 1

    # Calculate the number of hours Kira was away from home
    hours = intervals * 4

    result = hours
    return result

print(solution())