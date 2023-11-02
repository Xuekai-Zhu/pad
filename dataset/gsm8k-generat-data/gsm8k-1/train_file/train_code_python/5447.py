def solution():
    """Jim ran 16 miles in 2 hours while Frank ran 20 miles in 2 hours. How many more miles did Frank run than Jim in an hour?"""
    jim_distance = 16
    jim_time = 2
    frank_distance = 20
    frank_time = 2
    jim_speed = jim_distance / jim_time
    frank_speed = frank_distance / frank_time
    difference = frank_speed - jim_speed
    result = difference
    return result

print(solution())