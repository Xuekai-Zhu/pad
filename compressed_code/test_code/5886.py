def solution():
    
    starting_seashells = 180
    given_to_friends = 40
    given_to_brothers = 30
    remaining_seashells = starting_seashells - given_to_friends - given_to_brothers
    sold_seashells = remaining_seashells / 2
    seashells_left = remaining_seashells - sold_seashells
    result = seashells_left
    return result

print(solution())