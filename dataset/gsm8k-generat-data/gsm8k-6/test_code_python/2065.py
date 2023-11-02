def solution():
    # Calculate the total number of eggs laid by Myrtle's hens in 7 days
    total_eggs = 3 * 3 * 7  # 3 hens lay 3 eggs a day for 7 days

    # Subtract the number of eggs taken by the neighbor and the dropped eggs
    remaining_eggs = total_eggs - 12 - 5

    result = remaining_eggs
    return result

print(solution())