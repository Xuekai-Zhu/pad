def solution():
    """Nigella is a realtor who earns a base salary of $3,000 a month plus a 2% commission on every house she sells. One month, Nigella sells 3 houses and earns $8,000 total. House B costs three times as much as House A. House C cost twice as much as House A minus $110,000. How much did House A cost?"""
    # Define Nigella's base salary and commission rate
    base_salary = 3000
    commission_rate = 0.02

    # Define the number of houses sold and total earnings
    houses_sold = 3
    total_earnings = 8000

    # Calculate the total commission earned
    commission_earned = (total_earnings - base_salary) / commission_rate

    # Calculate the average commission per house
    commission_per_house = commission_earned / houses_sold

    # Calculate the cost of House B and House C
    house_b_cost = commission_per_house * 3
    house_c_cost = (commission_per_house - 110000) / 2

    # Calculate the cost of House A
    house_a_cost = (commission_per_house - house_b_cost - house_c_cost)

    result = round(house_a_cost)
    return result

print(solution())