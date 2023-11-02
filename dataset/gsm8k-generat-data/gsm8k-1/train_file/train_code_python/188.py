def solution():
    """Thor is 13 times older than Captain America. Captain America is 7 times older than Peter Parker, and Ironman is 32 years older than Peter Parker. How old is Ironman if Thor is 1456 years old?"""
    thor_age = 1456
    ca_age = thor_age / 13
    pp_age = ca_age / 7
    im_age = pp_age + 32
    result = im_age
    return result

print(solution())