def solution():
    """Jonny climbed 1269 stairs last week. Julia climbed 7 less than one-third of that amount. How many stairs did Julia and Jonny climb together?"""
    jonny_climb = 1269
    julia_climb = (1/3 * jonny_climb) - 7
    total_climb = jonny_climb + julia_climb
    result = total_climb
    return result

print(solution())