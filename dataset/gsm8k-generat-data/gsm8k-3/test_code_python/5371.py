def solution():
    """Martha has 20 apples. She decided to split them among her friends. Jane got 5 apples from her, and James got 2 more than Jane. How many more apples would Martha need to give away to be left with only 4 of them?"""
    # Initialize the number of apples Martha has
    marthas_apples = 20

    # Calculate the number of apples Jane got
    janes_apples = 5

    # Calculate the number of apples James got
    james_apples = janes_apples + 2

    # Calculate the total number of apples given away
    total_given_away = janes_apples + james_apples

    # Calculate the number of apples left with Martha
    marthas_apples_left = marthas_apples - total_given_away

    # Calculate the number of apples she needs to give away to have only 4 left
    apples_to_give_away = marthas_apples_left - 4

    # Display the number of apples Martha needs to give away
    result = apples_to_give_away
    return result

print(solution())