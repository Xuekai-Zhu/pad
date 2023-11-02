def solution():
    toilet_paper_cost = 12
    groceries_cost = 2 * toilet_paper_cost
    money_left = 50 - toilet_paper_cost - groceries_cost
    boots_cost = 3 * money_left
    money_needed_for_boots = 2 * boots_cost
    money_needed_per_sister = money_needed_for_boots / 2
    result = money_needed_per_sister
    return result

print(solution())