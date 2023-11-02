def solution():
    # Find the common multiples of 2, 3, and 4 until they overlap
    i = 1
    while True:
        time = i * 2
        if time % 3 == 0 and time % 4 == 0:
            result = time
            break
        i += 1
            
    return result

print(solution())