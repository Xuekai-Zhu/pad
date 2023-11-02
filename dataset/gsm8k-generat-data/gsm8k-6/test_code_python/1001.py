def solution():
    # Calculate the total money earned by selling the orchids and Chinese money plants
    total_orchid_money = 20 * 50
    total_chinese_money_plant_money = 15 * 25
    total_earnings = total_orchid_money + total_chinese_money_plant_money

    # Calculate the total money spent on paying the workers and buying new pots
    total_worker_salary = 2 * 40
    total_pot_cost = 150
    total_expense = total_worker_salary + total_pot_cost

    # Calculate the money left from the earnings
    money_left = total_earnings - total_expense
    result = money_left
    return result

print(solution())