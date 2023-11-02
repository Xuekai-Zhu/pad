def solution():
    """Carson runs a carpool for five of his friends. The five of them cover all the gas expenses to compensate Carson for his time. Their total commute is 21 miles one way, gas costs $2.50/gallon, Carson's car gets 30 miles/gallon, and they commute to work 5 days a week, 4 weeks a month. How much does each person pay toward gas monthly?"""
    num_people = 5
    commute_distance = 21 * 2  # roundtrip distance
    gas_price = 2.5
    gas_mileage = 30
    days_per_week = 5
    weeks_per_month = 4
    total_distance = commute_distance * days_per_week * weeks_per_month
    gallons_used = total_distance / gas_mileage
    total_cost = gallons_used * gas_price
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())