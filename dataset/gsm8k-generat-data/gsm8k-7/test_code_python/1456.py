def solution():
    num_days = 5
    
    jackson_fishes_per_day = 6
    jonah_fishes_per_day = 4
    george_fishes_per_day = 8
    
    # Calculate the total number of fishes caught by each person
    jackson_total_fishes = jackson_fishes_per_day * num_days
    jonah_total_fishes = jonah_fishes_per_day * num_days
    george_total_fishes = george_fishes_per_day * num_days
    
    # Calculate the total number of fishes caught by the team
    total_fishes = jackson_total_fishes + jonah_total_fishes + george_total_fishes
    result = total_fishes
    return result

print(solution())