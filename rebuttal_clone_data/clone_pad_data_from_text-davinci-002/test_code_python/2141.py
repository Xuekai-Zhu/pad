def solution():
    acres_mowed = 8
    riding_mower_acres = 0.75
    push_mower_acres = 1
    riding_mower_hours = riding_mower_acres / 2
    push_mower_hours = push_mower_acres
    total_hours = riding_mower_hours + push_mower_hours
    result = total_hours
    return result

print(solution())