def solution():
    
    total_glasses_sold = 32
    julie_glasses_sold = 14
    micah_glasses_sold = (total_glasses_sold - julie_glasses_sold) / 3
    difference = julie_glasses_sold - micah_glasses_sold
    result = difference
    return result

print(solution())