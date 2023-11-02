def solution():
    starting_elevation = 400
    rate_of_descent = 10
    time_of_descent = 5

    # Calculate the change in elevation due to descent
    change_in_elevation = rate_of_descent * time_of_descent

    # Calculate the new elevation after descent
    new_elevation = starting_elevation - change_in_elevation
    result = new_elevation
    return result

print(solution())