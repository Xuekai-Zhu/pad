def solution():
     first_hose = 50
     second_hose = 70
     hours_first_hose = 3
     hours_second_hose = 2
     total_hours = hours_first_hose + hours_second_hose
     total_gallons = (first_hose * hours_first_hose) + (second_hose * hours_second_hose)
     gallons_per_hour = total_gallons / total_hours
     result = gallons_per_hour
     return result

print(solution())