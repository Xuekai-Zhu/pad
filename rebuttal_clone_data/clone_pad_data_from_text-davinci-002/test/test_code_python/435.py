def solution():
    total_money = 60
    cost_of_hummus = 5 * 2
    cost_of_chicken = 20
    cost_of_bacon = 10
    cost_of_vegetables = 10
    cost_of_apples = 2
    remaining_money = total_money - (cost_of_hummus + cost_of_chicken + cost_of_bacon + cost_of_vegetables)
    number_of_apples = remaining_money / cost_of_apples
    result = number_of_apples
    
    return result

print(solution())