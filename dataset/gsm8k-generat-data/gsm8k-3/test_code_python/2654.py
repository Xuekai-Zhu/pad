def solution():
    """Jack bought 55 apples. He wants to give 10 to his father and then equally share the remaining apples between him and his 4 friends. How many apples will each of them get?"""
    # Define the number of apples Jack bought
    total_apples = 55

    # Define the number of apples Jack gives to his father
    father_apples = 10

    # Calculate the number of apples remaining
    remaining_apples = total_apples - father_apples

    # Calculate the number of apples each of them will get
    num_people = 4 + 1 # Jack and his 4 friends
    apples_per_person = remaining_apples // num_people

    # Display the number of apples each person will get
    result = apples_per_person
    return result

print(solution())