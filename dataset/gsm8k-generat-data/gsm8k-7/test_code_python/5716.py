def solution():
    tablespoons_per_cup = 0.5
    joanie_cups = 3
    mitchell_cups = 4
    miles_davis_cups = 6 / 2  # split between two people
    cliff_cups = 3

    # Calculate the total cups of popcorn needed
    total_cups = joanie_cups + mitchell_cups + miles_davis_cups + cliff_cups

    # Calculate the total tablespoons of popcorn kernels needed
    total_tablespoons = total_cups * tablespoons_per_cup
    result = total_tablespoons
    return result

print(solution())