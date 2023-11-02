def solution():
    """Jack bought 55 apples. He wants to give 10 to his father and then equally share the remaining apples between him and his 4 friends. How many apples will each of them get?"""
    # Define the total number of apples
    total_apples = 55

    # Subtract the number of apples given to Jack's father
    remaining_apples = total_apples - 10

    # Divide the remaining apples equally between Jack and his 4 friends
    apples_per_person = remaining_apples / 5

    # Return the result
    result = apples_per_person
    return result

print(solution())