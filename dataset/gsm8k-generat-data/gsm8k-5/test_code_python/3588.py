def solution():
    end_bedbugs = 810  # number of bedbugs after four days
    starting_bedbugs = end_bedbugs / (3 ** 4)  # divide by 3 four times to get the starting number of bedbugs
    result = starting_bedbugs
    return result

print(solution())