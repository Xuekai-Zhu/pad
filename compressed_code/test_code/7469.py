def solution():
    
    cups_per_jug = 40
    cups_per_student_per_day = 10
    total_cups_needed = 200 * cups_per_student_per_day
    jugs_needed = total_cups_needed // cups_per_jug
    if total_cups_needed % cups_per_jug != 0:
        jugs_needed += 1
    result = jugs_needed
    return result

print(solution())