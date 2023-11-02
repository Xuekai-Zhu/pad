def solution():
    # Calculate the total number of eggs
    total_eggs = 10 * 6 * 2  # 10 chickens, 6 eggs each per week, 2 weeks
    # Calculate the total number of dozens
    total_dozen = total_eggs / 12
    # Calculate the total amount of money Jane will make
    total_money = total_dozen * 2  # the price of one dozen is $2
    result = total_money
    return result

print(solution())