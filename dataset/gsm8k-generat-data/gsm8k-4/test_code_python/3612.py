def solution():
    """Carl buys index cards for his class. He gives each student 10 index cards. He teaches 6 periods a day and each class has 30 students. If a 50 pack of index cards cost $3 how much did he spend on them all?"""
    # Define the number of index cards per student and per pack
    INDEX_CARDS_PER_STUDENT = 10
    INDEX_CARDS_PER_PACK = 50

    # Define the number of periods per day and the number of students per class
    PERIODS_PER_DAY = 6
    STUDENTS_PER_CLASS = 30

    # Calculate the total number of packs needed for one day
    packs_per_day = PERIODS_PER_DAY * (STUDENTS_PER_CLASS / INDEX_CARDS_PER_PACK)

    # Calculate the total cost for one day
    cost_per_day = packs_per_day * 3

    result = cost_per_day
    return result

print(solution())