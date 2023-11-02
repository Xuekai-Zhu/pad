def solution():
    """Carly collected 7 starfish with 5 arms each and one seastar with 14 arms. How many arms do the animals she collected have in total?"""
    starfish_num = 7
    starfish_arms = 5
    seastar_arms = 14
    total_arms = (starfish_num * starfish_arms) + seastar_arms
    result = total_arms
    return result

print(solution())