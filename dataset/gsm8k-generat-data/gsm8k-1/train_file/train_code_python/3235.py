def solution():
    """Ricky has 40 roses. His little sister steals 4 roses. If he wants to give away the rest of the roses in equal portions to 9 different people, how many roses will each person get?"""
    initial_roses = 40
    stolen_roses = 4
    remaining_roses = initial_roses - stolen_roses
    num_people = 9
    roses_per_person = remaining_roses / num_people
    result = roses_per_person
    return result

print(solution())