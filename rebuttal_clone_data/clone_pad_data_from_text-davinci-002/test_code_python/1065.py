def solution():
    raw_squat = 600
    sleeves = 30
    wraps = (raw_squat * 0.25) + raw_squat
    difference = wraps - (raw_squat + sleeves)
    result = difference
    return result

print(solution())