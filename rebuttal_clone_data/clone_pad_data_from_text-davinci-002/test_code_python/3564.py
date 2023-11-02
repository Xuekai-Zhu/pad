def solution():
    cost_bread = 50
    cost_ham = 150
    cost_cake = 200
    total_cost = cost_bread + cost_ham + cost_cake
    percent_ham_bread = (cost_ham + cost_bread) / total_cost
    result = percent_ham_bread
    return result

print(solution())