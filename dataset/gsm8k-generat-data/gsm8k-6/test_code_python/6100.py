def solution():
    # Calculate the number of grandchildren Grandma Olga has
    total_granddaughters = 3 * 5 * 6  # each son has 5 daughters and Grandma Olga has 3 sons
    total_grandsons = 3 * 6  # each daughter has 6 sons and Grandma Olga has 3 daughters
    total_grandchildren = total_granddaughters + total_grandsons
    result = total_grandchildren
    return result

print(solution())