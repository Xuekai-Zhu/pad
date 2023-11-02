def solution():
    # Calculate the total number of fruit Tanya bought
    total_fruit = 6 + 4 + 2 + x  # We don't know how many plums Tanya bought, represented by x
    
    # Calculate the number of fruit that fell out of the bag
    lost_fruit = total_fruit / 2
    
    # Calculate the number of fruit remaining in the bag
    remaining_fruit = 9
    
    # Calculate the number of plums Tanya bought
    plums = remaining_fruit - lost_fruit - (6 + 4 + 2)
    result = plums
    return result

print(solution())