def solution():
    # Define the number of flowers each daughter planted
    initial_flowers_per_daughter = 5

    # Calculate the total number of flowers
    total_flowers = 2 * initial_flowers_per_daughter + 20 - 10

    # Define the number of baskets
    num_baskets = 5

    # Calculate the number of flowers in each basket
    flowers_per_basket = total_flowers / num_baskets
    result = flowers_per_basket
    return result

print(solution())