def solution():
    """Janet counts 30 crows on the powerlines and 60% more hawks than crows. How many birds does she count total?"""
    crow_count = 30
    hawk_count = int(crow_count * 1.6)
    total_bird_count = crow_count + hawk_count
    result = total_bird_count
    return result

print(solution())