def solution():
    # Calculate the total number of gallons needed to fill the pool
    total_gallons = 100 * 50  # hose runs at 100 gallons per hour and pool takes 50 hours to fill

    # Calculate the total cost of the water needed to fill the pool
    total_cost = (total_gallons / 10) * 0.01  # water costs 1 cent for 10 gallons

    result = total_cost
    return result

print(solution())