def solution():
    
    candy_count = 36
    monday_wednesday_candies = 2 * 2
    rest_of_week_candies = 5 * 1
    candies_per_week = monday_wednesday_candies + rest_of_week_candies
    weeks_to_finish = candy_count / candies_per_week
    result = weeks_to_finish
    return result

print(solution())