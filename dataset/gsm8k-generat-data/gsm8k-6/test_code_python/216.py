def solution():
    # Calculate the total amount of money Missy put in the bank after doubling the amount every year
    total_money = 450
    fourth_year_money = total_money / 15  # the fourth year, Missy put in double the amount from the third year, which was double the amount from the second year, which was double the amount from the first year
    third_year_money = fourth_year_money / 2
    second_year_money = third_year_money / 2
    first_year_money = second_year_money / 2
    result = first_year_money
    return result

print(solution())