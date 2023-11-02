def solution():
    """Wilma has a garden with 3 types of flowers. The garden has 6 rows, with 13 flowers in each row. Wilma has 12 yellow flowers, two times more green flowers, and the rest consist of red flowers. How many red flowers does Wilma have?"""
    # Define the total number of flowers in the garden
    total_flowers = 6 * 13

    # Calculate the number of green flowers
    green_flowers = 12 * 2

    # Calculate the number of yellow and green flowers
    yellow_green_flowers = 12 + green_flowers

    # Calculate the number of red flowers
    red_flowers = total_flowers - yellow_green_flowers

    # return the result
    result = red_flowers
    return result

print(solution())