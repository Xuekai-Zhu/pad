def solution():
    # Calculate the number of cans given away on the first day
    day1_cans = 500

    # Calculate the number of cans Carla had to restock after the first day
    day1_restock = 1500

    # Calculate the number of cans given away on the second day
    day2_cans = 1000 * 2

    # Calculate the number of cans Carla had to restock after the second day
    day2_restock = 3000

    # Calculate the total cans given away
    total_given_away = day1_cans + day2_cans

    # Return the total cans given away
    return total_given_away

print(solution())