def solution():
    ricciana_run = 20
    ricciana_jump = 4
    margarita_run = 18
    margarita_jump = (ricciana_jump * 2) - 1
    difference = (margarita_run + margarita_jump) - (ricciana_run + ricciana_jump)
    result = abs(difference)
    return result

print(solution())