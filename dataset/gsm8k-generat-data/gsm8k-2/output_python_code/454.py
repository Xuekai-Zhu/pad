def solution():
    """An amoeba reproduces by fission, splitting itself into two separate amoebae. An amoeba reproduces every two days. How many days will it take one amoeba to divide into 16 amoebae?"""
    original_amoebae = 1
    final_amoebae = 16
    division_time = 2
    num_divisions = 0
    while original_amoebae < final_amoebae:
        original_amoebae *= 2
        num_divisions += 1
    
    result = num_divisions * division_time
    return result

print(solution())