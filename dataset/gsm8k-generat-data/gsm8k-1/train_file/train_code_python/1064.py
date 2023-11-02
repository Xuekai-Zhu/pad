def solution():
    """John has a raw squat of 600 pounds without sleeves or wraps. Sleeves add 30 pounds to his lift. Wraps add 25% to his squat. How much more pounds does he get out of wraps versus sleeves."""
    raw_squat = 600
    sleeve_boost = 30
    wrap_boost = raw_squat * 0.25
    wrap_lifting_weight = raw_squat + wrap_boost
    sleeve_lifting_weight = raw_squat + sleeve_boost
    difference = wrap_lifting_weight - sleeve_lifting_weight
    result = difference
    return result

print(solution())