def solution():
    """Alisa biked 12 miles per hour for 4.5 hours. Stanley biked at 10 miles per hour for 2.5 hours. How many miles did Alisa and Stanley bike in total?"""
    alisa_speed = 12
    alisa_time = 4.5
    stanley_speed = 10
    stanley_time = 2.5
    alisa_distance = alisa_speed * alisa_time
    stanley_distance = stanley_speed * stanley_time
    total_distance = alisa_distance + stanley_distance
    result = total_distance
    return result

print(solution())