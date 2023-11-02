def solution():
    cost_of_cans = 6 * 2
    cost_of_bread = 2 * 5
    cost_of_cereal = 2 * 3
    cost_of_milk = 2 * 4
    total_cost = cost_of_cans + cost_of_bread + cost_of_cereal + cost_of_milk
    number_of_bills = total_cost / 10
    result = number_of_bills
    return result

print(solution())