def solution():
    # Convert given weights to pounds
    mario_oranges = 8/16  # 8 ounces of oranges = 0.5 pounds
    lydia_apples = 24/16  # 24 ounces of apples = 1.5 pounds
    total_fruit = 8  # given total fruit weight is 8 pounds
    peach_weight = total_fruit - mario_oranges - lydia_apples  # peach weight is the difference between total fruit weight and Mario's oranges and Lydia's apples
    result = peach_weight
    return result

print(solution())