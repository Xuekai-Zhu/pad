def solution():
    total_bears = 20
    bears_taken = 8
    bears_given = ((total_bears - bears_taken) / 3) + 10
    result = bears_given
    return result

print(solution())