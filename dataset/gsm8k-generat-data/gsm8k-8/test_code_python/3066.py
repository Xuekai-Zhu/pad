def solution():
    # Let's assume Martin initially had x number of fruits
    x = 2 * 50  # as given, Martin has twice as many oranges as limes
    remaining_fruits = 0.5 * x  # Martin ate half of the number of fruits he had
    initial_fruits = x + remaining_fruits  # adding the remaining fruits to the initial number of fruits
    result = initial_fruits
    return result

print(solution())