def solution():
    total_rows = 50
    flowers_per_row = 400
    flowers_cut = 60
    flowers_remaining = total_rows * flowers_per_row * (1 - (flowers_cut / 100))
    result = flowers_remaining
    
    return result

print(solution())