def solution():
    
    first_guess = 100
    second_guess = 8 * first_guess
    third_guess = second_guess - 200
    fourth_guess = (first_guess + second_guess + third_guess) / 3 + 25
    result = fourth_guess
    return result

print(solution())