def solution():
    """Jason bought a new bookcase that can hold a maximum of 80 pounds of weight. Jason has 70 hardcover books that each weigh half a pound, 30 textbooks that each weigh 2 pounds, and 3 knick-knacks that each weight 6 pounds. How many pounds over the bookcase's weight limit is this total collection of items?"""
    # Define the maximum weight the bookcase can hold
    MAX_WEIGHT = 80

    # Calculate the total weight of the books
    book_weight = 70 * 0.5 + 30 * 2

    # Calculate the total weight of the knick-knacks
    knick_knack_weight = 3 * 6

    # Calculate the total weight of all items
    total_weight = book_weight + knick_knack_weight

    # Calculate how many pounds over the bookcase's weight limit this is
    over_weight = total_weight - MAX_WEIGHT

    # Display the result
    result = over_weight
    return result

print(solution())