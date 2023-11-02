def solution():
    num_eggs_collected = 8 * 12
    num_market_eggs = 3 * 12
    num_mall_eggs = 5 * 12
    num_pie_eggs = 4 * 12

    # Calculate the total number of eggs used
    total_used_eggs = num_market_eggs + num_mall_eggs + num_pie_eggs

    # Calculate the number of eggs remaining
    num_remaining_eggs = num_eggs_collected - total_used_eggs

    result = num_remaining_eggs
    return result

print(solution())