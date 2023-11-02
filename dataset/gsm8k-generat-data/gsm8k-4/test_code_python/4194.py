def solution():
    """
    Henry believes in the famous phrase, "An apple a day, keeps the doctor away." If a box contains 14 apples, how many weeks can Henry and his brother spend eating 3 boxes of apples if they each eat 1 apple a day?
    """
    # Define the number of apples in a box and the number of boxes
    APPLES_PER_BOX = 14
    NUM_BOXES = 3

    # Define the number of apples Henry and his brother eat each day
    APPLES_PER_DAY = 2

    # Calculate the total number of apples
    total_apples = APPLES_PER_BOX * NUM_BOXES

    # Calculate the number of days it will take to eat all the apples if they each eat 1 apple a day
    days_to_eat_all = total_apples / APPLES_PER_DAY

    # Calculate the number of weeks it will take
    weeks_to_eat_all = days_to_eat_all / 7

    # Return the result
    result = round(weeks_to_eat_all)
    return result

print(solution())