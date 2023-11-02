def solution():
    """Barbeck has two times as many guitars as Steve, but Davey has three times as many guitars as Barbeck. If there are 27 guitars altogether, how many guitars does Davey have?"""
    # Define the number of guitars Barbeck has as "x"
    x = None

    # Calculate the number of guitars Steve has as "y"
    y = x / 2

    # Calculate the number of guitars Davey has as "z"
    z = x * 3

    # Set the total number of guitars to 27
    total_guitars = 27

    # Use the equation x + y + z = 27 to solve for x and z
    x = total_guitars / 7
    z = x * 3

    result = z
    return result

print(solution())