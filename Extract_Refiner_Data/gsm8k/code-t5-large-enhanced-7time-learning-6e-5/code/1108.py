def solution():
    
    # Define the initial amount of apples
    initial_apples = 12

    # Calculate the amount of apples Peter wants
    peter_apples = initial_apples / 4

    # Calculate the amount of apples Paul wants
    paul_apples = initial_apples / 3

    # Calculate the amount of apples James will have left
    remaining_apples = initial_apples - peter_apples - paul_apples

    # Display the amount of apples James will have left
    result = remaining_apples
    return result

print(solution())