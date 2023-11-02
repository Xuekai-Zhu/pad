def solution():
    
    raw_squat = 600
    sleeve_boost = 30
    wrap_boost = raw_squat * 0.25
    wrap_lifting_weight = raw_squat + wrap_boost
    sleeve_lifting_weight = raw_squat + sleeve_boost
    difference = wrap_lifting_weight - sleeve_lifting_weight
    result = difference
    return result

print(solution())