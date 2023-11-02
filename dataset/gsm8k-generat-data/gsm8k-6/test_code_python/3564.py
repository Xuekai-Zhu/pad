def solution():
    total_cost = 50 + 150 + 200  # total cost of all items
    cost_bread_ham = 50 + 150  # cost of bread and ham
    percent_bread_ham = (cost_bread_ham / total_cost) * 100  # percentage of cost that is bread and ham
    result = percent_bread_ham
    return result

print(solution())