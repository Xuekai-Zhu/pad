def solution():
     blouses = 100
     dots_per_blouse = 20
     ml_per_dot = 10
     total_ml = blouses * dots_per_blouse * ml_per_dot
     bottles_needed = total_ml / 400
     result = bottles_needed
     return result

print(solution())