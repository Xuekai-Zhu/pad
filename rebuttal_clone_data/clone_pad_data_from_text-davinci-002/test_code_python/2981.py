def solution():
    Jackie_daily_distance = 2
    Jessie_daily_distance = 1.5
    days = 6
    Jackie_total_distance = Jackie_daily_distance * days
    Jessie_total_distance = Jessie_daily_distance * days
    Jackie_distance_advantage = Jackie_total_distance - Jessie_total_distance
    result = Jackie_distance_advantage
    return result

print(solution())