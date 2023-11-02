def solution():
    """Thomas started saving for a car almost 2 years ago. For the first year, his weekly allowance was $50. In the second year, he got a job that pays $9 an hour at a coffee shop and worked 30 hours a week, so his parents discontinued his allowance. If the car he wants to buy is $15,000 and he spends $35 a week on himself, how much more money does Thomas need to buy the car by the end of the 2 years?"""
    year_one_savings = 50 * 52
    year_two_savings = (9 * 30 - 35) * 52
    total_savings = year_one_savings + year_two_savings
    car_cost = 15000
    remaining_cost = car_cost - total_savings
    result = remaining_cost
    return result

print(solution())