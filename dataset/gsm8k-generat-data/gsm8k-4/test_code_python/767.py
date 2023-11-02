def solution():
    """There were 40 kids on Lake Pleasant. A fourth of the kids went tubing, but only half of the tubers went rafting. How many of the kids who joined the rafting excursion were also on the tubing excursion?"""
    # Define the total number of kids
    total_kids = 40

    # Calculate the number of kids who went tubing
    tubing_kids = total_kids / 4

    # Calculate the number of kids who went rafting after tubing
    rafting_tubing_kids = tubing_kids / 2

    # Calculate the total number of kids who went rafting
    rafting_kids = total_kids - tubing_kids + rafting_tubing_kids

    # Calculate the number of kids who went both tubing and rafting
    tubing_rafting_kids = rafting_tubing_kids

    # return the result
    result = tubing_rafting_kids
    return result

print(solution())