def solution():
     total_meters = 600
     given_away = 5*20
     meters_needed = 5
     dresses_made = (total_meters - given_away) / meters_needed
     result = dresses_made
     
     return result

print(solution())