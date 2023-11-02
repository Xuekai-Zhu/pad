def solution():
    
    initial_size = 100
    donated_size = 0 
    for i in range(2):
        donated_size += initial_size/2
        initial_size /= 2 
    result = donated_size
    return result

print(solution())