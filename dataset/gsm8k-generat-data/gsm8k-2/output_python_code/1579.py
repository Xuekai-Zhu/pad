def solution():
    """Wilma has a garden with 3 types of flowers. The garden has 6 rows, with 13 flowers in each row. Wilma has 12 yellow flowers, two times more green flowers, and the rest consist of red flowers. How many red flowers does Wilma have?"""
    total_flowers = 6 * 13
    yellow_flowers = 12
    green_flowers = 2 * yellow_flowers
    red_flowers = total_flowers - yellow_flowers - green_flowers
    result = red_flowers
    return result

print(solution())