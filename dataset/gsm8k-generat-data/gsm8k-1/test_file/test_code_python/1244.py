def solution():
    """Jason works as a salesperson at a car dealership. He needs to sell 15 cars this month to earn a big bonus. He knows based on historical averages, that for every 25 telephone calls he makes to potential customers, he gets one person to come into the car dealership to look at new cars. And for every two customers that come into the car dealership, one will buy a car. Based on these average numbers, how many telephone calls would Jason need to make to sell 15 cars and earn his bonus?"""
    cars_needed = 15
    calls_per_person = 25
    conversion_rate = 2
    customers_needed = cars_needed * conversion_rate
    people_needed = customers_needed * conversion_rate
    calls_needed = people_needed * calls_per_person
    result = calls_needed
    return result

print(solution())