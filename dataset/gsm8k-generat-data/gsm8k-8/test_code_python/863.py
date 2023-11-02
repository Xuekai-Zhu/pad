def solution():
    # Define the number of students who like french fries, burgers, and both
    fries = 15
    burgers = 10
    both = 6

    # Calculate the number of students who only like french fries
    fries_only = fries - both

    # Calculate the number of students who only like burgers
    burgers_only = burgers - both

    # Calculate the number of students who don't like either food
    neither = 25 - (fries_only + burgers_only + both)

    result = neither
    return result

print(solution())