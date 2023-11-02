def solution():
    snail1_speed = 2
    snail2_speed = snail1_speed * 2
    snail3_speed = snail2_speed * 5
    snail1_time = 20
    snail3_time = snail1_time * (snail3_speed / snail1_speed)
    result = snail3_time
    return result

print(solution())