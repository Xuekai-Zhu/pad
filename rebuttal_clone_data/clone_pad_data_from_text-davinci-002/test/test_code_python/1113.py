def solution():
     hours_housesitting = 10
     hourly_wage_housesitting = 15
     hours_walking = 3
     hourly_wage_walking = 22
     total_hours = hours_housesitting + hours_walking
     total_wage = hours_housesitting * hourly_wage_housesitting + hours_walking * hourly_wage_walking
     return total_wage

print(solution())