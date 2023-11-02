def solution():
    number_of_wheels = 0  # Initialize total number of wheels to zero

    # Each car has 4 wheels, so add 8 to the total
    number_of_wheels += 8

    # The riding lawnmower has 4 wheels, so add 4 to the total
    number_of_wheels += 4

    # Timmy's bike and each of his parents' bikes have 2 wheels each, so add 6 to the total
    number_of_wheels += 6

    # Joey's tricycle has 3 wheels, so add 3 to the total
    number_of_wheels += 3

    # Timmy's dad's unicycle has 1 wheel, so add 1 to the total
    number_of_wheels += 1

    result = number_of_wheels
    return result

print(solution())