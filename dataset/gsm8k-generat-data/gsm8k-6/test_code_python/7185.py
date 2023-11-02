def solution():
    # Calculate the total number of eggs laid by the chickens
    total_eggs = 20 * 6  # each chicken lays 6 eggs
    egg_cartons = total_eggs // 12  # calculate the number of egg cartons needed, using integer division
    result = egg_cartons
    return result

print(solution())