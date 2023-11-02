def solution():
    
    jim_seashells = 27
    carlos_seashells = jim_seashells - 5
    carrey_seashells = carlos_seashells * 2
    total_seashells = jim_seashells + carlos_seashells + carrey_seashells
    each_person_gets = total_seashells / 2
    result = each_person_gets
    return result

print(solution())