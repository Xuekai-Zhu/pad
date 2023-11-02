def solution():
    # Calculate the total number of eggs in 8 weeks
    total_eggs = 46 * 6 * 8  # 46 chickens, each giving 6 eggs/week, 8 weeks

    # Calculate the number of dozens of eggs
    dozens_of_eggs = total_eggs / 12

    # Calculate the total money made from selling the eggs
    total_money = dozens_of_eggs * 3

    result = total_money
    return result

print(solution())