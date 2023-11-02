def solution():
    """The world record for longest fingernails is 26 inches. Sandy, who just turned 12 this month, has a goal for tying the record. Her fingernails are 2 inches long. Her fingernails grow at a rate of one-tenth of an inch per month. How old will she be when she achieves the world record?"""

    # Define the starting length of Sandy's fingernails and the world record
    SANDY_START_LENGTH = 2
    WORLD_RECORD_LENGTH = 26

    # Define the growth rate of Sandy's fingernails
    GROWTH_RATE = 0.1

    # Initialize the number of months and Sandy's age in years
    months = 0
    age = 12

    # Calculate the number of months it will take Sandy to reach the world record
    while SANDY_START_LENGTH < WORLD_RECORD_LENGTH:
        SANDY_START_LENGTH += GROWTH_RATE
        months += 1
        if months % 12 == 0:
            age += 1

    # Display Sandy's age when she achieves the world record
    result = age
    return result

print(solution())