def solution():
    # Find out how many crackers Mona has
    # If Marcus has 3 times as many as Mona, then Mona has 1/3 of Marcus' amount
    mona_crackers = 27 / 3

    # Find out how many crackers Nicholas has
    # If Nicholas has 6 more than Mona, then add 6 to Mona's amount
    nicholas_crackers = mona_crackers + 6

    result = nicholas_crackers
    return result

print(solution())