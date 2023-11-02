def solution():
    # Calculate the height of Janice's first throw
    janice_first_throw = 20 - 4

    # Calculate the height of Christine's second throw
    christine_second_throw = 20 + 10

    # Calculate the height of Janice's second throw
    janice_second_throw = janice_first_throw * 2

    # Calculate the height of Christine's third throw
    christine_third_throw = christine_second_throw + 4

    # Calculate the height of Janice's third throw
    janice_third_throw = 20 + 17

    # Find the highest throw between Christine and Janice
    highest_throw = max(christine_third_throw, janice_third_throw)

    result = highest_throw
    return result

print(solution())