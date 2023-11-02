def solution():
    # Calculate the total number of crayons Annie has
    total_crayons = 21 + 36 + (36/2) # Bobby gave her half the amount she already had in her locker (36 crayons)
    
    # Calculate the number of crayons Annie gives to her sister Mary
    mary_crayons = total_crayons / 3
    
    result = mary_crayons
    return result

print(solution())