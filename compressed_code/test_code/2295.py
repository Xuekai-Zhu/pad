def solution():
    
    total_shots = 20
    made_shots = int(total_shots * 0.8)
    missed_shots = total_shots - made_shots
    result = missed_shots
    return result

print(solution())