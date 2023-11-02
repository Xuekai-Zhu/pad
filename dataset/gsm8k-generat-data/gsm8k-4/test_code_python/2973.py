def solution():
    """Jean has 60 stuffies. She keeps 1/3 of them and then gives away the rest. She gives 1/4 of what she gave away to her sister Janet. How many stuffies did Janet get?"""
    # Define the initial number of stuffies
    initial_stuffies = 60

    # Calculate the number of stuffies Jean keeps
    kept_stuffies = initial_stuffies / 3

    # Calculate the number of stuffies Jean gives away
    given_stuffies = initial_stuffies - kept_stuffies

    # Calculate the number of stuffies Janet gets
    janet_stuffies = given_stuffies * (1/4)

    # return the result
    result = janet_stuffies
    return result

print(solution())