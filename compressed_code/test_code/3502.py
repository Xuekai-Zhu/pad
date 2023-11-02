def solution():
    
    total_bars = 7 + (2 * 7)
    total_squares = total_bars * 8
    squares_per_student = total_squares // 24
    result = squares_per_student
    return result

print(solution())