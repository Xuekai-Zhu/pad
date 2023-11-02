def solution():
    # Calculate the total number of popsicle sticks brought by boys and girls
    total_popsicle_sticks_boys = 10 * 15  # 10 boys brought 15 popsicle sticks each
    total_popsicle_sticks_girls = 12 * 12  # 12 girls brought 12 popsicle sticks each
    
    # Calculate the difference between the total number of popsicle sticks brought by boys and girls
    difference = total_popsicle_sticks_boys - total_popsicle_sticks_girls
    result = difference
    return result

print(solution())