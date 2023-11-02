def solution():
    """There were three jars of candy in the cabinet. The jar of peanut butter candy had 4 times as much candy as the jar of grape candy. The jar of grape candy had 5 more pieces of candy than the jar of banana candy. How many pieces of candy did the peanut butter jar have if the banana jar had 43?"""
    # Define the number of pieces of candy in the banana jar
    banana_candy = 43

    # Calculate the number of pieces of candy in the grape jar
    grape_candy = banana_candy + 5

    # Calculate the number of pieces of candy in the peanut butter jar
    peanut_butter_candy = grape_candy * 4

    # Display the number of pieces of candy in the peanut butter jar
    result = peanut_butter_candy
    return result

print(solution())