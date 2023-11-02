def solution():
    
    total_candies = 36
    candies_eaten_on_mon_wed = 2 * 2  
    candies_eaten_on_other_days = 5 * 1  
    candies_eaten_per_week = candies_eaten_on_mon_wed + candies_eaten_on_other_days
    weeks_to_finish_candies = total_candies // candies_eaten_per_week
    result = weeks_to_finish_candies
    return result

print(solution())