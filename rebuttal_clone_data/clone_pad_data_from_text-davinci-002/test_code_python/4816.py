def solution():
    fried_chicken = 11
    lyndee_ate = 1
    friends_ate = 2
    total_ate = lyndee_ate + (friends_ate * 2)
    friends_over = (total_ate - fried_chicken) / 2
    result = friends_over
    return result

print(solution())