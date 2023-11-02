def solution():
     money_per_mile_last_year = 4
     money_per_mile_this_year = 2.75
     money_collected_last_year = 44
     miles_walked_last_year = money_collected_last_year / money_per_mile_last_year
     money_collected_this_year = money_per_mile_this_year * miles_walked_last_year
     miles_walked_this_year = money_collected_this_year / money_per_mile_this_year
     result = miles_walked_this_year - miles_walked_last_year
     return result

print(solution())