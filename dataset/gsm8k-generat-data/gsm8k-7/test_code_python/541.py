def solution():
    num_sisters = 2
    younger_sister_gift_cost = 15 * 4  # 4 dolls that cost $15 each
    total_gift_budget = younger_sister_gift_cost * num_sisters

    lego_set_cost = 20
    num_lego_sets = total_gift_budget // lego_set_cost  # use integer division to get whole number of lego sets

    result = num_lego_sets
    return result

print(solution())