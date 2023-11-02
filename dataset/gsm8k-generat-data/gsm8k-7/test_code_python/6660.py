def solution():
    meat_pounds = 20
    meat_price = 5.0

    fruits_veggies_pounds = 15
    fruits_veggies_price = 4.0

    bread_pounds = 60
    bread_price = 1.5

    janitor_hours = 10
    janitor_pay = 10 * 1.5  # time-and-a-half pay

    total_cost = (meat_pounds * meat_price) + (fruits_veggies_pounds * fruits_veggies_price) + (bread_pounds * bread_price) + janitor_pay

    hours_worked = total_cost / 8  # minimum wage is $8/hour

    result = hours_worked
    return result

print(solution())