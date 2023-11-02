def solution():
    # Calculate the total biking time per day (to and from work)
    biking_time = 2 * 2

    # Calculate the cost of one pack of snacks based on the time spent biking
    snack_cost = biking_time * 10

    # Calculate the total cost of 50 packs of snacks
    total_cost = snack_cost * 50

    result = total_cost
    return result

print(solution())