def solution():
    carrying_capacity = 80
    first_pickup_point = carrying_capacity * (3/5)
    second_pickup_point = 50
    total_people = first_pickup_point + second_pickup_point
    people_left_behind = total_people - carrying_capacity
    result = people_left_behind
    return result

print(solution())