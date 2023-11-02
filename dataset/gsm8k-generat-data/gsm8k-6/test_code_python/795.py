def solution():
    # Calculate the total number of sandwiches Samson ate on Monday
    sandwiches_monday = 3 + 2*3  # Samson ate 3 sandwiches at lunch and twice as many at dinner
    sandwiches_tuesday = 1  # Samson only ate 1 sandwich on Tuesday
    sandwiches_difference = sandwiches_monday - sandwiches_tuesday  # calculate the difference
    result = sandwiches_difference
    return result

print(solution())