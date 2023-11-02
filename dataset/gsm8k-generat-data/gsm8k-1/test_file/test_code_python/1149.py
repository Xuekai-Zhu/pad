def solution():
    """Carlos, Jim and Carrey were at the beach playing and they decided to gather some seashells. Jim collected 27 seashells, which was 5 more than what Carlos collected. Carlos collected twice as many as Carrey. They gathered all their seashells and divided them equally between themselves. How many did each person get?"""
    jim_seashells = 27
    carlos_seashells = jim_seashells - 5
    carrey_seashells = carlos_seashells / 2
    total_seashells = jim_seashells + carlos_seashells + carrey_seashells
    num_people = 3
    each_person_gets = total_seashells / num_people
    result = each_person_gets
    return result

print(solution())