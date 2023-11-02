def solution():
    total_apples = 64  # Jane picked 64 apples
    baskets = 4  # She sorted them into 4 different baskets
    stolen_apples = 3 * baskets  # Her sister took 3 apples from each basket

    # Calculate the number of apples in each basket now
    remaining_apples = (total_apples - stolen_apples) / baskets
    result = remaining_apples
    return result

print(solution())