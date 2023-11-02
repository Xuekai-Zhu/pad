def solution():
    # Define the total number of problems
    total_problems = 20

    # Define the number of problems for each person
    bill_problems = total_problems
    ryan_problems = 2 * bill_problems
    frank_problems = 3 * ryan_problems

    # Define the number of types of problems
    num_types = 4

    # Calculate the number of problems of each type for Frank
    type_problems = frank_problems // num_types

    # Define the result as a dictionary with the number of problems of each type for Frank
    result = {'type_1': type_problems, 'type_2': type_problems, 'type_3': type_problems, 'type_4': type_problems}

    return result

print(solution())