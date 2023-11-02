def solution():
    """Matt's entire family was going to spend the week at the lake house for vacation.  Matt's family included his mom, dad, his older brother and his wife and their 4 kids.  His Uncle Joe and his wife were also coming and would bring their 3 kids.  The house only sleeps 4 people.  Everyone else would sleep 2 to a tent outside.  How many tents would they need?"""
    # Define the number of people in each family group
    MATT_FAMILY = 1 + 1 + 1 + 1 + 4
    BROTHER_FAMILY = 1 + 1 + 4
    UNCLE_FAMILY = 1 + 1 + 3

    # Define the number of people who can sleep in the house
    HOUSE_CAPACITY = 4

    # Calculate the total number of people
    total_people = MATT_FAMILY + BROTHER_FAMILY + UNCLE_FAMILY

    # Calculate the number of people who will need to sleep in tents
    tent_people = total_people - HOUSE_CAPACITY

    # Calculate the number of tents needed
    tents_needed = (tent_people + 1) // 2

    # Display the number of tents needed
    result = tents_needed
    return result

print(solution())