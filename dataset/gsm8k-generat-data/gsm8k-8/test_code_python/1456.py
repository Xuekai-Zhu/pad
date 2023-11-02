def solution():
    # Define the number of days and the number of fishes each person caught per day
    days = 5
    jackson_fishes_per_day = 6
    jonah_fishes_per_day = 4
    george_fishes_per_day = 8

    # Calculate the total number of fishes each person caught
    jackson_total_fishes = jackson_fishes_per_day * days
    jonah_total_fishes = jonah_fishes_per_day * days
    george_total_fishes = george_fishes_per_day * days

    # Calculate the total number of fishes caught by the team
    total_fishes = jackson_total_fishes + jonah_total_fishes + george_total_fishes
    result = total_fishes
    return result

print(solution())