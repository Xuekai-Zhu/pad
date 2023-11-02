def solution():
    oprah_ivy_degrees = ["Duke"]
    ivy_league_universities = ["Harvard", "Yale", "Princeton", "Columbia", "Dartmouth", "Cornell", "Brown"]
    overlap = [degree for degree in oprah_ivy_degrees if degree in ivy_league_universities]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())