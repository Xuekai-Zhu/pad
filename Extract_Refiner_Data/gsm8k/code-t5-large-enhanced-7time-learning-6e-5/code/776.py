def solution():
    
    emma_points = 10 * 8
    emma_collected = 5 * 3
    emma_score = emma_points + emma_collected
    ava_points = 30 * (emma_points - emma_points)
    ava_score -= ava_points
    emma_score += emma_points
    ava_score -= emma_points
    emma_score -= emma_points
    ava_score -= ava_points
    difference = abs(ava_score - emma_score)
    result = difference
    return result

print(solution())