def solution():
    """Johnny makes his signature crab dish 40 times a day. It uses 1.5 pounds of crab meat. Crab meat sells for $8 per pound. How much does he spend in a week if he is closed 3 days a week?"""
    # Define the number of times Johnny makes his signature crab dish in a week
    crab_dish_per_week = 40 * 7

    # Define the amount of crab meat needed per dish
    crab_meat_per_dish = 1.5

    # Calculate the amount of crab meat needed in a week
    crab_meat_per_week = crab_dish_per_week * crab_meat_per_dish

    # Calculate the total cost of crab meat in a week
    crab_meat_cost = crab_meat_per_week * 8

    # Calculate the amount of money Johnny saves by being closed 3 days a week
    savings = crab_meat_cost * (3/7)

    # Calculate the final cost of crab meat in a week
    final_cost = crab_meat_cost - savings
    
    result = final_cost
    return result

print(solution())