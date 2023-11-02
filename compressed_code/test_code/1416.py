def solution():
    
    class_size = 24
    before_lunch = class_size // 3
    after_lunch = before_lunch + 10
    remaining = class_size - after_lunch
    result = remaining
    return result

print(solution())