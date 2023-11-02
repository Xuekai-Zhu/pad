def solution():
    """Frank invites his friends over to play video games. He bakes a pan of brownies before he arrives. He cuts 6 even columns and 3 even rows into the pan of brownies. If there are 6 people, including Frank, in total, how many brownies can they each eat?"""
    columns = 6
    rows = 3
    total_brownies = columns * rows
    people = 6
    brownies_per_person = total_brownies / people
    result = brownies_per_person
    return result

print(solution())