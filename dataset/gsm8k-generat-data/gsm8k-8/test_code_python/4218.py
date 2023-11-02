def solution():
    # Define Kirill's height as x
    x = None

    # Define Kirill's brother's height as x + 14
    brother_height = x + 14

    # Define the total height as x + (x + 14) = 112
    total_height = x + brother_height

    # Solve for x
    x = (112 - 14) / 2

    result = x
    return result

print(solution())