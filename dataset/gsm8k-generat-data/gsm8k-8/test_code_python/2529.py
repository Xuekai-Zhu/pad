def solution():
    # Calculate the number of hot dogs the first competitor can eat in 5 minutes
    competitor1 = 10 * 5

    # Calculate the number of hot dogs the second competitor can eat in 5 minutes
    competitor2 = 3 * competitor1

    # Calculate the number of hot dogs the third competitor can eat in 5 minutes
    competitor3 = 2 * competitor2

    result = competitor3
    return result

print(solution())