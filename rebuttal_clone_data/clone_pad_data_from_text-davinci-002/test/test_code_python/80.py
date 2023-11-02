def solution():
    
    minutes_in_hour = 60
    minutes_per_episode_jeopardy = 20
    minutes_per_episode_wheel = minutes_per_episode_jeopardy * 2
    episodes_jeopardy = 2
    episodes_wheel = 2
    total_minutes_jeopardy = minutes_per_episode_jeopardy * episodes_jeopardy
    total_minutes_wheel = minutes_per_episode_wheel * episodes_wheel
    total_minutes = total_minutes_jeopardy + total_minutes_wheel
    total_hours = total_minutes / minutes_in_hour
    result = total_hours
    
    return result

print(solution())