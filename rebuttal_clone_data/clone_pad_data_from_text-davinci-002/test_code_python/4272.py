def solution():
    total_servings = 12
    chicken_needed = 4.5
    stuffing_needed = 24
    ounces_per_serving = (chicken_needed / total_servings) + (stuffing_needed / total_servings)
    result = ounces_per_serving
    return result

print(solution())