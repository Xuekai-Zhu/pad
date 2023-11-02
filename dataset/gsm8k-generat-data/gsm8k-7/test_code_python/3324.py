def solution():
    initial_money = 50
    toilet_paper_cost = 12
    grocery_cost = toilet_paper_cost * 2
    remaining_money = initial_money - toilet_paper_cost - grocery_cost
    cost_per_pair_of_boots = remaining_money / 3
    total_cost_of_two_pairs_of_boots = cost_per_pair_of_boots * 2
    money_to_add_each = (total_cost_of_two_pairs_of_boots - remaining_money) / 2
    result = money_to_add_each
    return result

print(solution())