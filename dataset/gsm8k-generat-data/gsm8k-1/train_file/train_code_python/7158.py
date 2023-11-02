def solution():
    """Ishmael, Ponce, and Jalen measured their weight and realized Ishmael was 20 pounds heavier than Ponce and that Ponce was 10 pounds lighter than Jalen. If Jalen weighed 160 pounds, calculate the average weight of the three?"""
    jalen_weight = 160
    ponce_weight = jalen_weight - 10
    ishmael_weight = ponce_weight + 20
    total_weight = jalen_weight + ponce_weight + ishmael_weight
    average_weight = total_weight / 3
    result = average_weight
    return result

print(solution())