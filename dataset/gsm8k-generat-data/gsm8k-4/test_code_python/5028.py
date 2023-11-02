def solution():
    """It takes 1 person working 10 hours to figure out the solution to a math problem. If you add a second person who's equally good at math, how long will the two of them have to work to solve the same problem?"""
    # Define the time it takes for one person to solve the problem and the number of people working on it
    time_one_person = 10
    num_people = 2

    # Calculate the time it takes for the two people working together to solve the problem
    time_two_people = time_one_person / num_people

    # return the result
    result = time_two_people
    return result

print(solution())