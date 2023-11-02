def solution():
    total_money = 960

    # Calculate the amount spent on textbooks
    textbook_cost = total_money / 2

    # Calculate the remaining amount of money
    remaining_money = total_money - textbook_cost

    # Calculate the amount spent on school supplies
    supplies_cost = remaining_money / 4

    # Calculate the final amount of money Derek has left
    final_money = remaining_money - supplies_cost
    result = final_money
    return result

print(solution())