def solution():
    # Calculate the total amount of caffeine in three cups of coffee
    caffeine_in_3_cups = 80 * 3

    # Calculate the amount of caffeine Lisa exceeded her goal by
    excess_caffeine = caffeine_in_3_cups - 200

    # Check if Lisa exceeded her goal
    if excess_caffeine > 0:
        result = excess_caffeine
    else:
        result = 0
    return result

print(solution())