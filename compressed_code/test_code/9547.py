def solution():
    
    athlete1_long_jump = 26
    athlete1_triple_jump = 30
    athlete1_high_jump = 7
    athlete2_long_jump = 24
    athlete2_triple_jump = 34
    athlete2_high_jump = 8
    athlete1_average_jump = (athlete1_long_jump + athlete1_triple_jump + athlete1_high_jump) / 3
    athlete2_average_jump = (athlete2_long_jump + athlete2_triple_jump + athlete2_high_jump) / 3
    winner_average_jump = max(athlete1_average_jump, athlete2_average_jump)
    result = winner_average_jump
    return result

print(solution())