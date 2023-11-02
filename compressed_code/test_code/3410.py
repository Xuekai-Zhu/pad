def solution():
    
    current_people = 200
    current_speed = 500
    while current_people < 400:
        current_people += 100
        current_speed /= 2
    result = current_speed
    return result

print(solution())