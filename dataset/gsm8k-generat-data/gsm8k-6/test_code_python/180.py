def solution():
    total_money = 960  # dollars
    textbooks_cost = total_money / 2  # half of the total money goes towards textbooks
    remaining_money = total_money - textbooks_cost  # money left after buying textbooks
    school_supplies_cost = remaining_money / 4  # a quarter of what is left goes towards school supplies
    money_left = remaining_money - school_supplies_cost  # the total amount of money left
    result = money_left
    return result

print(solution())