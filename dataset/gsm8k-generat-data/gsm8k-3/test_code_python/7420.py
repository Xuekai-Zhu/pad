def solution():
    """Nikola is saving up for a bag of ant food before he can start his ant farm. He wants 400 ants in his farm. Each ant needs 2 ounces of food. Every ounce of ant food costs $.1. Nikola is saving up by raking leaves. He charges $5 to start a job and then he charges by the leaf. Each leaf he rakes costs 1 penny. He finally saved up enough money after he raked 6,000 leaves. How many jobs did he complete?"""
    # Define the number of ants Nikola wants in his farm and the food requirement per ant
    ANT_COUNT = 400
    FOOD_PER_ANT = 2

    # Define the cost of one ounce of ant food and the total cost for all the ants
    FOOD_PRICE_PER_OUNCE = 0.1
    TOTAL_FOOD_COST = ANT_COUNT * FOOD_PER_ANT * FOOD_PRICE_PER_OUNCE

    # Define the cost of starting a job and the cost per leaf raked
    JOB_START_COST = 5
    LEAF_COST = 0.01

    # Calculate the total cost of all the leaves raked
    LEAF_COUNT = 6000
    LEAF_COST_TOTAL = LEAF_COUNT * LEAF_COST

    # Calculate the total amount of money Nikola earned
    TOTAL_EARNED = TOTAL_FOOD_COST + LEAF_COST_TOTAL + JOB_START_COST

    # Calculate the number of jobs Nikola completed
    JOBS_COMPLETED = (TOTAL_EARNED - JOB_START_COST - TOTAL_FOOD_COST) / (LEAF_COST * LEAF_COUNT)

    # Display the number of jobs Nikola completed
    result = JOBS_COMPLETED
    return result

print(solution())