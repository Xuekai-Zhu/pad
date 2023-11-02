def solution():
     total_attendance = 50
     first_team_support = 40
     second_team_support = 34
     first_team_attendance = total_attendance * (first_team_support / 100)
     second_team_attendance = total_attendance * (second_team_support / 100)
     non_supporters = total_attendance - first_team_attendance - second_team_attendance
     result = non_supporters
     return result

print(solution())