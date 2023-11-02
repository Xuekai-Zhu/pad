def solution():
    """Colston knows that his teacher loves drinking coffee and one day wants to see how much she drinks each week. He sees that she has a 20-ounce thermos and when she makes her coffee she pours a 1/2 cup of milk in, and then fills the coffee to the top. She does this twice a day. After the five-day school week, he decides to tell her, and when she hears how much coffee she drinks, she decides to drink 1/4 of what she normally drinks. How many ounces of coffee does she now drink a week?"""
    # Define the volume of the thermos and the amount of milk added per cup
    THERMOS_CAPACITY = 20 # ounces
    MILK_PER_CUP = 0.5 # cups

    # Calculate the amount of coffee per cup
    COFFEE_PER_CUP = THERMOS_CAPACITY - MILK_PER_CUP

    # Calculate the amount of coffee per day
    COFFEE_PER_DAY = 2 * COFFEE_PER_CUP

    # Calculate the amount of coffee per week
    COFFEE_PER_WEEK = COFFEE_PER_DAY * 5

    # Calculate the amount of coffee the teacher will now drink
    NEW_COFFEE_PER_WEEK = COFFEE_PER_WEEK * 0.25

    result = NEW_COFFEE_PER_WEEK
    return result

print(solution())