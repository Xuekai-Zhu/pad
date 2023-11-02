def solution():
    """Carson runs a carpool for five of his friends. The five of them cover all the gas expenses to compensate Carson for his time. Their total commute is 21 miles one way, gas costs $2.50/gallon, Carson's car gets 30 miles/gallon, and they commute to work 5 days a week, 4 weeks a month. How much does each person pay toward gas monthly?"""
    total_commute = 21 * 2
    gas_cost = 2.5
    car_mileage = 30
    gas_used = total_commute / car_mileage
    monthly_gas_cost = gas_used * gas_cost * 5 * 4 / 5
    cost_per_person = monthly_gas_cost / 5
    result = cost_per_person
    return result

print(solution())