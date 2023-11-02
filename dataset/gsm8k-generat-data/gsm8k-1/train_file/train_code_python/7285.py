def solution():
    """Patrick has 4 hours less than twice the amount of time that Greg has left to finish his homework. 
    Greg has six hours less than Jacob left to finish his homework. If Jacob has 18 hours left to finish his homework, 
    calculate the total number of hours they all have left to finish their homework?"""
    
    jacob_time = 18
    greg_time = jacob_time - 6
    patrick_time = 2 * greg_time - 4
    total_time = jacob_time + greg_time + patrick_time
    
    return total_time

print(solution())