def solution():
    """Jason bought a new bookcase that can hold a maximum of 80 pounds of weight. Jason has 70 hardcover books that each weigh half a pound, 30 textbooks that each weigh 2 pounds, and 3 knick-knacks that each weight 6 pounds. How many pounds over the bookcase's weight limit is this total collection of items?"""
    # Define the maximum weight of the bookcase
    MAX_WEIGHT = 80

    # Calculate the total weight of the books and knick-knacks
    total_weight = (70 * 0.5) + (30 * 2) + (3 * 6)

    # Calculate the weight over the bookcase's weight limit
    weight_over_limit = total_weight - MAX_WEIGHT

    # return the result
    result = weight_over_limit
    return result

print(solution())