def solution():
    # Total number of fish in the tank before adding any
    total_fish = 280
    
    # Number of days in three weeks
    days = 21
    
    # Number of koi fish added each day
    koi_per_day = 2
    
    # Number of goldfish added each day
    goldfish_per_day = 5
    
    # Total number of goldfish after three weeks
    total_goldfish = 200
    
    # Calculate the total number of goldfish added over the three weeks
    total_goldfish_added = goldfish_per_day * days
    
    # Calculate the total number of koi fish added over the three weeks
    total_koi_added = total_fish - (total_goldfish + total_goldfish_added)
    
    # Calculate the total number of koi fish in the tank after three weeks
    total_koi = total_koi_added + (koi_per_day * days)
    
    result = total_koi
    return result

print(solution())