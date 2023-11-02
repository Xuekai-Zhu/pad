def solution():
    """Wilma has a garden with 3 types of flowers. The garden has 6 rows, with 13 flowers in each row. Wilma has 12 yellow flowers, two times more green flowers, and the rest consist of red flowers. How many red flowers does Wilma have?"""
    # Calculate the total number of flowers in the garden
    total_flowers = 6 * 13

    # Calculate the number of green flowers
    green_flowers = 2 * 12

    # Calculate the number of red flowers
    red_flowers = total_flowers - 12 - green_flowers

    # Display the number of red flowers
    result = red_flowers
    return result

print(solution())