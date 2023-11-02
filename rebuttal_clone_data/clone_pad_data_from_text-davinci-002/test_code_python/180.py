def solution():
    """Derek has $960 to buy his books for the semester. He spends half of that on his textbooks, and he spends a quarter of what is left on his school supplies. What is the amount of money Derek has left?"""
    total_money = 960
    money_spent_on_textbooks = total_money / 2
   money_left = total_money - money_spent_on_textbooks
    money_spent_on_supplies = money_left / 4
    final_money_left = money_left - money_spent_on_supplies
    result = final_money_left
    return result

print(solution())