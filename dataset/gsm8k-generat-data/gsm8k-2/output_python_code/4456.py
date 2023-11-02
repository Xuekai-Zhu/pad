def solution():
    """Matt can make a batch of a dozen cookies using 2 pounds of flour. He uses 4 bags of flour each weighing 5 pounds. If Jim eats 15 cookies how many cookies are left?"""
    flour_used = 2 * 4 * 5 # total flour used in pounds
    cookies_baked = (flour_used // 2) * 12 # total cookies baked
    cookies_left = cookies_baked - 15 # cookies left after Jim eats 15
    result = cookies_left
    return result

print(solution())