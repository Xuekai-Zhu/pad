def solution():
    """Two tribes of soldiers gathered for a battle. The number of women was double the number of cannoneers. There were 63 cannoneers. None of the cannoneers were women. The total number of men is twice the number of women. How many people in total are there?"""
    cannoneers = 63
    women = cannoneers * 2
    men = women * 2
    total_people = cannoneers + women + men
    result = total_people
    return result

print(solution())