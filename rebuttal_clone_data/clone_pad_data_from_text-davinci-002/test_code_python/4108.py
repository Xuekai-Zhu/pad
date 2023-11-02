def solution():
     total_time = 8
     baseball_practice = 5
     dinner_time = 45
     homework_time = 30
     cleaning_room = 30
     taking_out_trash = 5
     emptying_dishwasher = 10
     
     latest_start_time = total_time - (baseball_practice + dinner_time + homework_time + cleaning_room + taking_out_trash + emptying_dishwasher)
     
     result = latest_start_time
     return result

print(solution())