def solution():
    """Thor is 13 times older than Captain America. Captain America is 7 times older than Peter Parker, and Ironman is 32 years older than Peter Parker. How old is Ironman if Thor is 1456 years old?"""
    thor_age = 1456
    cap_age = thor_age / 13
    peter_age = cap_age / 7
    ironman_age = peter_age + 32
    result = ironman_age
    return result

print(solution())