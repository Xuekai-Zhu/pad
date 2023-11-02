def solution():
    """A local farmer is paying 4 kids to help plant rows of corn. Every row of corn contains 70 ears. A bag of corn seeds contains 48 seeds and you need 2 seeds per ear of corn. He pays the kids $1.5 per row. Afterward, the kids are so hungry that they end up spending half their money on dinner. The dinner cost $36 per kid. How many bags of corn seeds did each kid use?"""
    # Define the number of kids, ears of corn per row, seeds per ear, seeds per bag, and cost per row
    NUM_KIDS = 4
    EARS_PER_ROW = 70
    SEEDS_PER_EAR = 2
    SEEDS_PER_BAG = 48
    ROW_COST = 1.5

    # Calculate the total number of rows planted by all the kids
    total_rows = 0
    for i in range(NUM_KIDS):
        rows_planted = int(input(f"How many rows did kid {i+1} plant? "))
        total_rows += rows_planted

    # Calculate the total number of ears of corn planted
    total_ears = total_rows * EARS_PER_ROW

    # Calculate the total number of seeds used
    total_seeds = total_ears * SEEDS_PER_EAR

    # Calculate the total number of bags used
    total_bags = total_seeds // SEEDS_PER_BAG

    # Calculate the total cost of the rows planted
    total_cost = total_rows * ROW_COST

    # Calculate the cost of dinner per kid
    dinner_cost = 36

    # Calculate the amount spent on dinner by all the kids
    total_dinner_cost = NUM_KIDS * (dinner_cost / 2)

    # Calculate the remaining money for the kids after dinner
    remaining_money = total_cost - total_dinner_cost

    # Calculate the amount spent on seeds per kid
    seed_cost = remaining_money / NUM_KIDS

    # Calculate the number of bags used per kid
    bags_per_kid = seed_cost / (SEEDS_PER_BAG * ROW_COST)

    result = bags_per_kid
    return result

print(solution())