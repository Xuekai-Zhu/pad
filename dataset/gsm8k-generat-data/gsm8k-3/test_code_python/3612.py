def solution():
    """Carl buys index cards for his class.  He gives each student 10 index cards.  He teaches 6 periods a day and each class has 30 students.  If a 50 pack of index cards cost $3 how much did he spend on them all?"""
    # Define the number of index cards each student receives
    INDEX_CARDS_PER_STUDENT = 10

    # Define the number of periods Carl teaches each day
    PERIODS_PER_DAY = 6

    # Define the number of students in each class
    STUDENTS_PER_CLASS = 30

    # Define the number of index cards per pack
    INDEX_CARDS_PER_PACK = 50

    # Define the cost per pack of index cards
    COST_PER_PACK = 3

    # Calculate the total number of index cards needed
    total_index_cards = PERIODS_PER_DAY * STUDENTS_PER_CLASS * INDEX_CARDS_PER_STUDENT

    # Calculate the number of packs of index cards needed
    packs_needed = (total_index_cards // INDEX_CARDS_PER_PACK) + 1

    # Calculate the total cost
    total_cost = packs_needed * COST_PER_PACK

    # Display the total cost
    result = total_cost
    return result

print(solution())