def solution():
    """An amoeba reproduces by fission, splitting itself into two separate amoebae. An amoeba reproduces every two days. How many days will it take one amoeba to divide into 16 amoebae?"""
    num_amoebae = 16
    days_per_division = 2
    num_divisions = 0
    
    while num_amoebae > 1:
        num_amoebae /= 2
        num_divisions += 1
        
    result = num_divisions * days_per_division
    return result

print(solution())