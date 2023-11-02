def solution():
    """Ali and Sara ate 80 small apples combined. Ali ate 4 times more apples than Sara. How many apples did Sara eat?"""
    # Calculate the total number of apples
    total_apples = 80

    # Let the number of apples Sara ate be x
    # Then the number of apples Ali ate is 4x
    # And their sum is the total number of apples
    # So we have x + 4x = total_apples
    # Solving for x gives x = total_apples / 5
    sara_apples = total_apples / 5

    # return the result
    result = sara_apples
    return result

print(solution())