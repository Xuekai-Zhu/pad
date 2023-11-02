def solution():
    # Find the cost of the corner light
    repair_fee = 10  
    corner_light = repair_fee * 2  

    # Find the cost of one brake disk
    brake_disk = corner_light * 3  

    # Find the total cost of the spare parts
    total_cost = corner_light + (brake_disk * 2)  

    # Find the amount of savings before the car broke
    savings_before = total_cost + repair_fee + 480  

    result = savings_before
    return result

print(solution())