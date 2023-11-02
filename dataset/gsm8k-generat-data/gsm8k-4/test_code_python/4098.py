def solution():
    """Colston knows that his teacher loves drinking coffee and one day wants to see how much she drinks each week. He sees that she has a 20-ounce thermos and when she makes her coffee she pours a 1/2 cup of milk in, and then fills the coffee to the top. She does this twice a day. After the five-day school week, he decides to tell her, and when she hears how much coffee she drinks, she decides to drink 1/4 of what she normally drinks. How many ounces of coffee does she now drink a week?"""
    # Define the volume of the thermos in ounces
    thermos_volume = 20

    # Define the volume of milk added to each cup of coffee
    milk_volume = 4  # 1/2 cup = 4 ounces

    # Define the volume of coffee in each cup
    coffee_volume = thermos_volume - milk_volume

    # Calculate the total volume of coffee consumed in a week before reducing intake
    weekly_coffee_volume = coffee_volume * 2 * 5  # 2 cups per day, 5 days per week

    # Calculate the total volume of coffee consumed in a week after reducing intake by 1/4
    new_weekly_coffee_volume = weekly_coffee_volume * 0.75

    # Return the result in ounces
    result = new_weekly_coffee_volume
    return result

print(solution())