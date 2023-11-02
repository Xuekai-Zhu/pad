def solution():
    """Janet has 60 less than four times as many siblings as Masud. Carlos has 3/4 times as many siblings as Masud. If Masud has 60 siblings, how many more siblings does Janet have more than Carlos?"""
    masud_siblings = 60
    janet_siblings = (4 * masud_siblings) - 60
    carlos_siblings = (3/4) * masud_siblings
    difference = janet_siblings - carlos_siblings
    result = difference
    return result

print(solution())