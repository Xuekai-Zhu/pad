def solution():
    # Define the initial number of people and cans of stew
    initial_people = 40
    initial_stew = 600

    # Calculate the number of people with a 30% decrease
    decreased_people = initial_people - (0.3 * initial_people)

    # Calculate the ratio of people and stew
    stew_ratio = initial_stew / initial_people

    # Calculate the number of stew cans needed for the decreased number of people
    decreased_stew = decreased_people * stew_ratio
    result = decreased_stew
    return result

print(solution())