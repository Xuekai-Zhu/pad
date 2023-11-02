def solution():
    anna_stamps = 37  # Anna had 37 stamps in her collection
    alison_stamps = 28  # Alison had 28 stamps in her collection
    jeff_stamps = 31  # Jeff had 31 stamps in his collection

    # Alison gives Anna half of her collection, which is 14 stamps
    anna_stamps += alison_stamps // 2  

    # Anna trades two bluebird stamps for one mountain stamp with Jeff
    anna_stamps -= 2  
    jeff_stamps += 2  
    jeff_stamps -= 1  
    anna_stamps += 1  

    result = anna_stamps  # The final number of stamps Anna has
    return result

print(solution())