def solution():
    total_money = 50
    toilet_paper_cost = 12
    groceries_cost = 2 * toilet_paper_cost
    remaining_money = total_money - toilet_paper_cost - groceries_cost
    boots_cost = 3 * remaining_money
    money_for_boots = total_money - toilet_paper_cost - groceries_cost
    if money_for_boots >= boots_cost:
        each_addition = boots_cost / 2
    else:
        each_addition = (money_for_boots + remaining_money) / 2
    result = each_addition
    return result

print(solution())