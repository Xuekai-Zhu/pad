def solution():
    puppy_cost = 10  # The cost of the puppy is $10
    food_per_day = 1/3  # The puppy eats 1/3 cup of food per day
    food_per_week = food_per_day * 7  # There are 7 days in a week
    food_for_3_weeks = food_per_week * 3  # Mark bought enough food for 3 weeks
    price_per_bag = 2  # A bag of food costs $2
    cups_per_bag = 3.5  # A bag of food contains 3.5 cups of food
    
    # Calculate the number of bags of food needed for 3 weeks
    bags_needed = food_for_3_weeks / cups_per_bag
    
    # Calculate the total cost
    total_cost = puppy_cost + (bags_needed * price_per_bag)
    result = total_cost
    return result

print(solution())