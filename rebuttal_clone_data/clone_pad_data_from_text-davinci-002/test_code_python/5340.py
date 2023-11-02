def solution():
    johns_time = 13
    johns_distance = 100
    johns_speed = johns_distance / johns_time
    james_time = johns_time - 2
    james_distance = johns_distance - 10
    james_speed = james_distance / james_time
    result = james_time + 2
    return result

print(solution())