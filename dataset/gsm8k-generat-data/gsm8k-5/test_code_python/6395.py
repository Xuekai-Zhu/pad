def solution():
    ladders_50_rungs = 10  # Jacob needs to build 10 ladders with 50 rungs
    ladders_60_rungs = 20  # Jacob needs to build 20 ladders with 60 rungs
    price_per_rung = 2  # Jacob charges $2 for every rung

    # Calculate the total number of rungs needed
    total_rungs = (ladders_50_rungs * 50) + (ladders_60_rungs * 60)

    # Calculate the total cost of the ladders
    total_cost = total_rungs * price_per_rung
    result = total_cost
    return result

print(solution())