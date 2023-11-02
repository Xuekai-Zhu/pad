def solution():
    """Frank invites his friends over to play video games. He bakes a pan of brownies before he arrives. He cuts 6 even columns and 3 even rows into the pan of brownies. If there are 6 people, including Frank, in total, how many brownies can they each eat?"""
    # Define the number of columns and rows in the pan of brownies
    columns = 6
    rows = 3

    # Calculate the total number of brownies
    total_brownies = columns * rows

    # Determine the number of brownies each person can eat
    brownies_per_person = total_brownies // 6

    # Return the result
    result = brownies_per_person
    return result

print(solution())