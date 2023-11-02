def solution():
    """Jake can wash his car with 1 bottle of car wash soap 4 times. 
    If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?"""
    # Define the number of car washes per bottle
    washes_per_bottle = 4

    # Define the cost of each bottle
    cost_per_bottle = 4.00

    # Define the total number of car washes
    total_washes = 20

    # Calculate the number of bottles needed for all the car washes
    total_bottles = total_washes / washes_per_bottle

    # Calculate the total cost of the car wash soap
    total_cost = total_bottles * cost_per_bottle

    # return the result
    result = total_cost
    return result

print(solution())