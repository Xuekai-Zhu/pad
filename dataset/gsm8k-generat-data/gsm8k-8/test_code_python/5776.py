def solution():
    # Calculate the number of applications needed
    num_applications = 16 // 2
    
    # Calculate the total amount of sunscreen needed
    total_sunscreen = num_applications * 3
    
    # Calculate the number of bottles needed
    num_bottles = total_sunscreen // 12 + 1
    
    # Calculate the cost of the sunscreen
    sunscreen_cost = num_bottles * 3.5
    
    result = sunscreen_cost
    return result

print(solution())