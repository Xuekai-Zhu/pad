def solution():
 
    generations = 3
    tails_length = 16
    for i in range(generations):
        tails_length = tails_length + (tails_length * 0.25)
    result = tails_length
    
    return result

print(solution())