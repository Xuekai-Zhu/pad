def solution():
    total_apples = 55  # the total number of apples bought by Jack
    apples_for_father = 10  # the number of apples Jack gives to his father
    remaining_apples = total_apples - apples_for_father  # the number of apples left for Jack and his friends to share
    apples_per_person = remaining_apples / 5  # equally shared between Jack and his 4 friends
    result = apples_per_person
    return result

print(solution())