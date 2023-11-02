def solution():
    """Jake sold 10 more stuffed animals than Thor. Quincy sold ten times as many stuffed animals as Thor. 
    If Quincy sold 200 stuffed animals, how many more stuffed animals did Quincy sell than Jake?"""
    quincy_sells = 200
    thor_sells = quincy_sells / 10
    jake_sells = thor_sells + 10
    difference = quincy_sells - jake_sells
    result = difference
    return result

print(solution())