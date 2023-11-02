def solution():
    """Marco has $24. Mary has $15. If Marco gives Mary half of what he has, Mary will have more than Marco. But Mary spends $5. How much more money does Mary have than Marco?"""
    # Define the initial amounts of money
    marco_money = 24
    mary_money = 15

    # Calculate the amount of money Marco gives to Mary
    marco_gives = marco_money / 2

    # Calculate Mary's new amount of money after receiving half of Marco's
    mary_new_money = mary_money + marco_gives

    # Calculate Mary's amount of money after spending $5
    mary_spends = 5
    mary_final_money = mary_new_money - mary_spends

    # Calculate the difference in money between Mary and Marco
    money_difference = mary_final_money - marco_money

    # return the result
    result = money_difference
    return result

print(solution())