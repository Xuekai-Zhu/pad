def solution():
    # Calculate the number of students who like basketball
    basketball = 0.4 * 250

    # Calculate the number of students who like chess
    chess = 0.1 * 250

    # Calculate the total number of students who like basketball or chess
    total = basketball + chess

    # Round the result to the nearest whole number
    result = round(total)
    return result

print(solution())