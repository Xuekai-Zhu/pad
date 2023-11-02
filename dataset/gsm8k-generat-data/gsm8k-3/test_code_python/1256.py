def solution():
    """Conor can chop 12 eggplants, 9 carrots, and 8 potatoes in a day. If he works 4 times a week, how many vegetables can he chop?"""
    # Define the number of vegetables Conor can chop in a day
    EGGPLANTS_PER_DAY = 12
    CARROTS_PER_DAY = 9
    POTATOES_PER_DAY = 8

    # Define the number of days Conor works in a week
    DAYS_PER_WEEK = 4

    # Calculate the total number of vegetables Conor can chop in a week
    total_eggplants = EGGPLANTS_PER_DAY * DAYS_PER_WEEK
    total_carrots = CARROTS_PER_DAY * DAYS_PER_WEEK
    total_potatoes = POTATOES_PER_DAY * DAYS_PER_WEEK

    # Display the total number of vegetables Conor can chop
    total_vegetables = total_eggplants + total_carrots + total_potatoes
    result = total_vegetables
    return result

print(solution())