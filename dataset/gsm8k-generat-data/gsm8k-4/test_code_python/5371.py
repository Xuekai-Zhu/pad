def solution():
    """Martha has 20 apples. She decided to split them among her friends. Jane got 5 apples from her, and James got 2 more than Jane. How many more apples would Martha need to give away to be left with only 4 of them?"""
    # Define the initial number of apples
    total_apples = 20

    # Subtract the number of apples given to Jane
    total_apples -= 5

    # Calculate the number of apples James got
    james_apples = 5 + 2

    # Subtract the number of apples given to James
    total_apples -= james_apples

    # Calculate the number of apples needed to be left with only 4
    apples_to_give_away = total_apples - 4

    result = apples_to_give_away
    return result

print(solution())