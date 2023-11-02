def solution():
    starting_elevation = 400  # John starts at an elevation of 400 feet
    rate_of_descent = 10  # John descends at a rate of 10 feet per minute
    time_of_descent = 5  # John descends for 5 minutes

    # Calculate John's final elevation after 5 minutes of descent
    final_elevation = starting_elevation - (rate_of_descent * time_of_descent)
    result = final_elevation
    return result

print(solution())