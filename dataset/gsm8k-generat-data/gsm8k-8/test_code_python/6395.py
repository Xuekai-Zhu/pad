def solution():
    # Define the number of ladders and rungs
    ladder1_count = 10
    ladder1_rungs = 50
    ladder2_count = 20
    ladder2_rungs = 60

    # Calculate the total number of rungs
    total_rungs = (ladder1_count * ladder1_rungs) + (ladder2_count * ladder2_rungs)

    # Calculate the total cost
    total_cost = total_rungs * 2
    result = total_cost
    return result

print(solution())