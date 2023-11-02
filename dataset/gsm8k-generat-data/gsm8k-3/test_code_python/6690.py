def solution():
    """A laboratory needs flasks, test tubes, and safety gear to carry out its experiments. They were given a $325 budget for the month. They bought $150 worth of flasks, spent two-thirds of that amount on test tubes, and used half of the test tube cost on safety gear. How many dollars of their budget remained?"""
    # Define the given budget and the cost of flasks
    BUDGET = 325
    FLASK_COST = 150

    # Calculate the cost of test tubes
    TEST_TUBE_COST = (2/3) * FLASK_COST

    # Calculate the cost of safety gear
    SAFETY_GEAR_COST = 0.5 * TEST_TUBE_COST

    # Calculate the total cost
    total_cost = FLASK_COST + TEST_TUBE_COST + SAFETY_GEAR_COST

    # Calculate the remaining budget
    remaining_budget = BUDGET - total_cost

    # Display the remaining budget
    result = remaining_budget
    return result

print(solution())