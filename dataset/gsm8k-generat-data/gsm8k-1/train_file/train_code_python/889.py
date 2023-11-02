def solution():
    """Javier is an Olympic javelin thrower. In the last Olympics, he threw the javelin three times. The first throw, he threw the javelin twice as far as he threw the javelin on his second throw, but only half as far as he threw it the third throw. If the sum of all three throws was 1050 meters, then how far, in meters, did he throw the javelin on his first throw?"""
    total_distance = 1050
    third_throw = (2/3) * total_distance
    second_throw = third_throw / 4
    first_throw = total_distance - (second_throw + third_throw)
    result = first_throw
    return result

print(solution())