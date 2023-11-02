def solution():
    hats_simpson = 15  # Fire chief Simpson has 15 hats
    hats_obrien = (2*hats_simpson) + 5  # Policeman O'Brien had 5 more than twice as many hats as Simpson before losing one
    hats_obrien_now = hats_obrien - 1  # Policeman O'Brien lost one of his hats

    result = hats_obrien_now
    return result

print(solution())