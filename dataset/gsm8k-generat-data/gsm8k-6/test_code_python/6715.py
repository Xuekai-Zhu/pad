def solution():
    # Calculate the height of each throw for Christine and Janice
    christine_throws = [20, 30, 34]  # heights of Christine's throws
    janice_throws = [16, 40, 37]  # heights of Janice's throws

    # Find the highest throw
    highest_throw = max(max(christine_throws), max(janice_throws))
    result = highest_throw
    return result

print(solution())