def solution():
    # Define the total penalty points Jerry already has
    total_points = 5*2 + 10*4

    # Define the penalty points for throwing things
    throw_points = 25

    # Calculate the maximum number of times Jerry can throw things without getting sent to the office
    max_throws = (100 - total_points) // throw_points
    result = max_throws
    return result

print(solution())