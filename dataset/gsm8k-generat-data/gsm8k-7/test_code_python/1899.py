def solution():
    cherry_candies = 0
    grape_candies = 0
    apple_candies = 0
    total_cost = 200
    candy_cost = 2.5

    # Cherry candies are the smallest quantity, so we use them as the base
    cherry_candies = (total_cost / candy_cost) / 6

    # Calculate the number of grape candies based on the ratio to cherry candies
    grape_candies = cherry_candies * 3

    # Calculate the number of apple candies based on the ratio to grape candies
    apple_candies = grape_candies * 2

    # Return the number of grape candies
    result = grape_candies
    return result

print(solution())