def solution():
    lollipops = 4
    packs_of_chocolate = 6
    cost_of_lollipops = 2
    cost_of_chocolate = cost_of_lollipops * 4
    total_cost = (lollipops * cost_of_lollipops) + (packs_of_chocolate * cost_of_chocolate)
    bills_given = 60
    change_received = bills_given - total_cost
    result = change_received
    return result

print(solution())