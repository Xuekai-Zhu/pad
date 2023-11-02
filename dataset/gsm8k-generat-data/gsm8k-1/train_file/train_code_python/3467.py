def solution():
    """Big Joe is the tallest player on the basketball team. He is one foot taller than Ben, who is one foot taller than Larry, who is one foot taller than Frank, who is half a foot taller than Pepe. If Pepe is 4 feet six inches tall, how tall is Big Joe, in feet?"""
    pepe_height = 4.5
    frank_height = pepe_height + 0.5
    larry_height = frank_height + 1
    ben_height = larry_height + 1
    big_joe_height = ben_height + 1
    result = big_joe_height
    return result

print(solution())