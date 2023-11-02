def solution():
    dolls_made = 12000
    accessories_per_doll = 2 + 3 + 1 + 5
    time_per_doll = 45
    time_per_accessory = 10
    total_time = (dolls_made * time_per_doll) + (accessories_per_doll * time_per_accessory)
    result = total_time
    return result

print(solution())