def solution():
    """Jake can wash his car with 1 bottle of car wash soap 4 times.  If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?"""
    # Define the variables
    BOTTLE_COST = 4.00
    BOTTLE_USES = 4
    WEEKS = 20

    # Calculate the number of bottles needed for 20 weeks
    bottles_needed = WEEKS // BOTTLE_USES
    if WEEKS % BOTTLE_USES != 0:
        bottles_needed += 1

    # Calculate the total cost of the car soap
    total_cost = bottles_needed * BOTTLE_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())