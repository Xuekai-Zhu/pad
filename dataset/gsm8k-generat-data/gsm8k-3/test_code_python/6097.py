def solution():
    """John has 25 horses. He feeds each horse twice a day and feeds them 20 pounds of food at each feeding. He buys half ton bags of food. How many of those will he have to buy in 60 days?"""
    # Define the amount of food consumed per horse per day
    FOOD_PER_HORSE_PER_DAY = 40  # 2 feedings x 20 pounds per feeding

    # Calculate the total amount of food consumed per day
    total_food_per_day = FOOD_PER_HORSE_PER_DAY * 25

    # Calculate the total amount of food consumed over 60 days
    total_food = total_food_per_day * 60

    # Calculate the number of half ton bags needed
    bags = total_food / 1000  # 1 ton = 2000 pounds, so 1/2 ton = 1000 pounds

    # Round up to the nearest whole bag
    bags = math.ceil(bags)

    # Display the number of bags needed
    result = bags
    return result

print(solution())