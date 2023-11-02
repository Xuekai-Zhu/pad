def solution():
    
    total_oranges = 180
    alice_oranges = 0.0
    emily_oranges = 0.0
    for i in range(total_oranges+1):
        if i*2 + i == total_oranges:
            alice_oranges = i*2
            emily_oranges = i
            break
    result = alice_oranges
    return result

print(solution())