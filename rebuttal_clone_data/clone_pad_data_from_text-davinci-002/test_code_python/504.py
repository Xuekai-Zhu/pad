def solution():
    hours_worked_march_to_august = 23
    hours_worked_september_to_february = 8
    total_hours_worked = hours_worked_march_to_august + hours_worked_september_to_february
    money_earned = 460
    video_game_console_cost = 600
    car_repair_cost = 340
    money_needed = video_game_console_cost - car_repair_cost
    hours_needed = money_needed / money_earned
    result = hours_needed
    return result

print(solution())