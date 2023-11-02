def solution():
     hours = 3
     math_hw = 45
     english_hw = 30
     science_hw = 50
     history_hw = 25
     project_time = hours - (math_hw + english_hw + science_hw + history_hw)
     result = project_time
     return result

print(solution())