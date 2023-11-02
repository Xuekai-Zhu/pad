def solution():
    iq_scores = [145, 145]
    mensa_minimums = {"Stanford-Binet": 132, "Cattell": 148}
    for test, minimum in mensa_minimums.items():
        if all(score >= minimum for score in iq_scores):
            result = "yes"
        else:
            result = "no"
            break
    return result

print(solution())