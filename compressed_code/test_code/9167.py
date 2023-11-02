def solution():
    
    initial_blondes = 30
    initial_total = 80
    added_blondes = 10
    final_total = initial_total + added_blondes
    final_blondes = initial_blondes + added_blondes
    final_black_haired = final_total - final_blondes
    result = final_black_haired
    return result

print(solution())