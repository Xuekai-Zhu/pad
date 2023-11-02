def solution():
    
    time = 2
    while True:
        if time % 2 == 0 and time % 3 == 0 and time % 4 == 0:
            result = time
            break
        time += 1

    return result

print(solution())