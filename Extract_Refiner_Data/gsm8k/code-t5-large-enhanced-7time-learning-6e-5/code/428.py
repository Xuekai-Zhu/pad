def solution():
    
    thaddeus_dragons = 100
    arthur_dragons = thaddeus_dragons * 0.75
    walter_dragons = arthur_dragons * 2
    bruce_dragons = walter_dragons / 5
    total_dragons = thaddeus_dragons + arthur_dragons + walter_dragons + bruce_dragons
    result = total_dragons
    return result

print(solution())