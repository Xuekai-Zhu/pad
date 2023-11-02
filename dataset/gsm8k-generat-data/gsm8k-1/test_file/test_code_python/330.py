def solution():
    """Nick, Richard, Jason and DJ each have paintball guns. DJ has 8 guns, Nick has 10 guns, RJ has 1 gun and Richard has 5 guns. If they were to share their guns equally, how many guns would each of them have?"""
    total_guns = 8 + 10 + 1 + 5
    num_people = 4
    guns_per_person = total_guns / num_people
    result = guns_per_person
    return result

print(solution())