def solution():
    """Troy had 300 straws. He fed 3/5 of the straws to the adult pigs and an equal number of straws to the piglets. If there were 20 piglets, how many straws did each piglet eat?"""
    total_straws = 300
    adult_pigs_straws = total_straws * (3/5)
    piglet_straws = adult_pigs_straws / 20
    result = piglet_straws
    return result

print(solution())