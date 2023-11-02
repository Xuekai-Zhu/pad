def solution():
    final_bedbugs = 810
    days = 4
    # Since the number of bedbugs triples every day, we can use the formula:
    # final_bedbugs = initial_bedbugs * 3^days
    initial_bedbugs = final_bedbugs / (3 ** days)
    result = initial_bedbugs
    return result

print(solution())