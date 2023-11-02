def solution():
     gallons_per_hour = 1000
     capacity = 240000
     hours_until_full = capacity / gallons_per_hour
     days_until_full = hours_until_full / 24
     result = days_until_full
     return result

print(solution())