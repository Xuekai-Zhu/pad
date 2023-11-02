def solution():
    """As soon as you enter the taxi, you pay a ride fee of $2. Michelle rode a taxi from her office to her home, which constitutes 4 miles. If the taxi charge per mile is $2.5, how much did pay Michelle pay in total for her ride?"""
    ride_fee = 2
    distance = 4
    charge_per_mile = 2.5
    total_cost = ride_fee + (distance * charge_per_mile)
    result = total_cost
    return result

print(solution())