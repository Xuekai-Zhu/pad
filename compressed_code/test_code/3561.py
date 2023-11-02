def solution():
    
    initial_bracelets = 0
    for i in range(5):
        initial_bracelets += 2
    initial_bracelets -= 3 
    for i in range(4):
        initial_bracelets += 3
    initial_bracelets -= 6 
    result = initial_bracelets
    return result

print(solution())