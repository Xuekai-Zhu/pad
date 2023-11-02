def solution():
    # Calculate the total number of sandwiches Samson ate on Monday
    sandwiches_monday = 3 + (2 * 3)  # Samson ate 3 at lunch and twice as many (6) at dinner

    # Calculate the total number of sandwiches Samson ate on Tuesday
    sandwiches_tuesday = 1  # Samson only ate one sandwich for breakfast

    # Calculate the difference in sandwiches eaten between Monday and Tuesday
    difference = sandwiches_monday - sandwiches_tuesday
    result = difference
    return result

print(solution())