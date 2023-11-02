def solution():
    """Frank invites his friends over to play video games. He bakes a pan of brownies before he arrives. He cuts 6 even columns and 3 even rows into the pan of brownies. If there are 6 people, including Frank, in total, how many brownies can they each eat?"""
    num_brownies = 6 * 3
    num_people = 6
    brownies_per_person = num_brownies / num_people
    result = brownies_per_person
    return result

print(solution())