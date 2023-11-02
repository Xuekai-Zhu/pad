def solution():
    
    total_time = 2*60 + 10
    elephant_time = 13
    penguin_time = 8 * elephant_time
    seal_time = total_time - elephant_time - penguin_time
    result = seal_time
    return result

print(solution())