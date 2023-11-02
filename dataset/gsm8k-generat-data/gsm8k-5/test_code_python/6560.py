def solution():
    total_fruit = 8  # The total weight of fruit is 8 pounds
    mario_oranges = 8 / 16  # Convert Mario's 8 ounces of oranges to pounds
    lydia_apples = 24 / 16  # Convert Lydia's 24 ounces of apples to pounds

    # Calculate the weight of peaches Nicolai ate
    nicolai_peaches = total_fruit - mario_oranges - lydia_apples

    result = nicolai_peaches
    return result

print(solution())