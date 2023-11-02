def solution():
    """Eighty-five cans were collected. LaDonna picked up 25 cans. Prikya picked up twice as many times as many cans as LaDonna. Yoki picked up the rest of the cans. How many cans did Yoki pick up?"""
    total_cans = 85
    ladonna_cans = 25
    prikya_cans = ladonna_cans * 2
    yoki_cans = total_cans - ladonna_cans - prikya_cans
    result = yoki_cans
    return result

print(solution())