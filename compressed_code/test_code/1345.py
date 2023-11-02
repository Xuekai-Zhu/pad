def solution():
    
    ricciana_run = 20
    ricciana_jump = 4
    ricciana_total = ricciana_run + ricciana_jump
    margarita_run = 18
    margarita_jump = 2 * ricciana_jump - 1
    margarita_total = margarita_run + margarita_jump
    difference = margarita_total - ricciana_total
    result = difference
    return result

print(solution())