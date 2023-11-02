def solution():
     hours = 3
     kilometers_per_hour = 5
     total_kilometers = 30
     kilometers_walked = hours * kilometers_per_hour
     remaining_kilometers = total_kilometers - kilometers_walked
     hours_needed = remaining_kilometers / kilometers_per_hour
     result = hours_needed
     return result

print(solution())