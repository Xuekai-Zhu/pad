def solution():
    number_of_sisters = 2
    gifts_ bought_for_younger_sister = 4
    cost_of_dolls = 15
    total_cost_for_younger_sister = gifts_bought_for_younger_sister * cost_of_dolls
    cost_of_legos = 20
    total_cost_for_older_sister = total_cost_for_younger_sister
    legos_bought_for_older_sister = total_cost_for_older_sister / cost_of_legos
    result = legos_bought_for_older_sister
    return result

print(solution())