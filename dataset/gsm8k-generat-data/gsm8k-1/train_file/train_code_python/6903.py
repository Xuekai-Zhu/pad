def solution():
    """Jonny climbed 1269 stairs last week. Julia climbed 7 less than one-third of that amount. How many stairs did Julia and Jonny climb together?"""
    jonny_climbed = 1269
    julia_climbed = (1/3)*jonny_climbed - 7
    total_climbed = jonny_climbed + julia_climbed
    result = total_climbed
    return result

print(solution())