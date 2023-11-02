def solution():
    """There were 40 kids on Lake Pleasant. A fourth of the kids went tubing, but only half of the tubers went rafting. How many of the kids who joined the rafting excursion were also on the tubing excursion?"""
    # Define the total number of kids
    total_kids = 40

    # Calculate the number of kids who went tubing
    tubing_kids = total_kids // 4

    # Calculate the number of tubers who went rafting
    rafting_kids = tubing_kids // 2

    # Display the number of kids who joined both the tubing and rafting excursion
    result = rafting_kids
    return result

print(solution())