def solution():
    
    dots_per_blouse = 20
    ml_per_dot = 10
    total_ml = dots_per_blouse * ml_per_dot * 100
    bottles_needed = total_ml / 400
    result = bottles_needed
    return result

print(solution())