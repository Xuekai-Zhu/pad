def solution():
    raw_squat = 600
    sleeves = 30
    wrap_increase = raw_squat * 0.25
    
    wrap_squat = raw_squat + wrap_increase
    sleeve_squat = raw_squat + sleeves
    
    difference = wrap_squat - sleeve_squat
    result = difference
    return result

print(solution())