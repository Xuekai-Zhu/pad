def solution():
    
    anna_stamps = 37
    alison_stamps = 28
    jeff_stamps = 31

    
    alison_stamps /= 2
    anna_stamps += alison_stamps

    
    anna_stamps -= 2
    jeff_stamps -= 1
    anna_stamps += 1

    result = anna_stamps
    return result

print(solution())