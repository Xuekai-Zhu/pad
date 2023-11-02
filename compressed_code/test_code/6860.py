def solution():
    
    joanna_initial = 40
    jacques_initial = 60
    purchased = 4 * (joanna_initial + jacques_initial)
    total = joanna_initial + jacques_initial + purchased
    each_get = total / 2
    result = each_get
    return result

print(solution())