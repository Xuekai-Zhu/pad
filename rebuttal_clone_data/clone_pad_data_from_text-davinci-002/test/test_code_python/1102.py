def solution():
     candies_per_hour = 50
     candies_needed = 4000
     hours_per_day = 10
     days_needed = candies_needed / (candies_per_hour * hours_per_day)
     result = days_needed
     return result

print(solution())