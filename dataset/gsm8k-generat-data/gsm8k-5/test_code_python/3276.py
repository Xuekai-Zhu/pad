def solution():
    # Let's assume the fastest speed of the rabbit is 'x'

    # Double the fastest speed and add 4
    step_1 = 2*x + 4

    # Double the previous result to get the final result of 188
    step_2 = 2*step_1

    # Solve for the value of x
    x = (step_2 - 4) / 2
    result = x
    return result

print(solution())