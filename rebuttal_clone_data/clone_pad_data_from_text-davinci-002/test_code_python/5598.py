def solution():
    total_towels = 60
    marys_towels = 24
    frances_towels = marys_towels / 4
    total_weight = total_towels * 16
    marys_weight = marys_towels * 16
    frances_weight = total_weight - marys_weight
    result = frances_weight
    return result

print(solution())