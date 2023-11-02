def solution():
    # Calculate the number of people who started at the gym
    starting_people = 19 - 5 + 2  # There are now 19 people, 5 came in, and 2 left

    # Calculate the number of people who were lifting weights at the start
    starting_weights = starting_people - (19 - starting_people)
    result = starting_weights
    return result

print(solution())