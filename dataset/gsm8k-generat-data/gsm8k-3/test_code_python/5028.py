def solution():
    """It takes 1 person working 10 hours to figure out the solution to a math problem.  If you add a second person who's equally good at math, how long will the two of them have to work to solve the same problem?"""
    # Define the number of people and the time it takes for one person to solve the problem
    num_people = 2
    time_per_person = 10

    # Calculate the total time it will take for both people to solve the problem
    total_time = time_per_person / num_people

    # Display the total time it will take for both people to solve the problem
    result = total_time
    return result

print(solution())