def solution():
    spider_eye_count = 8
    lenses_per_eye = 1
    total_lenses_needed = spider_eye_count * lenses_per_eye
    half_dozen = 6
    if total_lenses_needed > half_dozen:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())