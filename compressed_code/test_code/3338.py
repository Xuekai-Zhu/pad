def solution():
    
    initial_blondes = 30
    initial_total = 80
    new_blondes = 10
    total_with_new = initial_total + new_blondes
    new_black_haired = total_with_new - (initial_blondes + new_blondes)
    result = new_black_haired
    return result

print(solution())