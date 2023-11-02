def solution():
    passes_thrown = 50
    passes_right = passes_thrown / 2
    passes_left = passes_thrown - (passes_right + 2)
    result = passes_left
    
    return result

print(solution())