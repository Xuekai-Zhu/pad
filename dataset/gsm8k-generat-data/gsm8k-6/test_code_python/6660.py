def solution():
    # Calculate the cost of each type of wasted food and janitorial pay
    meat_cost = 20 * 5
    fruits_veggies_cost = 15 * 4
    bread_cost = 60 * 1.5
    janitorial_pay = 10 * 10 * 1.5

    # Calculate the total cost James has to work off
    total_cost = meat_cost + fruits_veggies_cost + bread_cost + janitorial_pay

    # Calculate the number of hours James has to work
    hours_to_work = total_cost / 8

    result = hours_to_work
    return result

print(solution())