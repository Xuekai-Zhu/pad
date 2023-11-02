def solution():
    # Define the initial height
    initial_height = 96

    # Initialize the height variable
    current_height = initial_height

    # Loop through the bounces, halving the height each time
    for i in range(5):
        current_height = current_height / 2

    result = current_height
    return result

print(solution())