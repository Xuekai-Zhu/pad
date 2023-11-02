def solution():
    bottles_per_crate = 12
    total_bottles = 130
    total_crates = 10
    bottles_leftover = total_bottles % bottles_per_crate
    result = bottles_leftover
    return result

print(solution())