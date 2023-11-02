def solution():
    initial_green_apples = 32
    initial_red_apples = initial_green_apples + 200
    new_green_apples = initial_green_apples + 340
    new_red_apples = initial_red_apples
    difference = new_green_apples - new_red_apples
    result = abs(difference)
    return result

# Note: We use the absolute value function (abs) to ensure we get a positive result, regardless of whether there are more green apples or red apples in the store.

print(solution())