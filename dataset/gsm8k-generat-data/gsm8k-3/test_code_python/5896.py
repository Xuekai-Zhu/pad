def solution():
    """There are 6 girls and 8 boys in the school play. If both parents of each kid attend the premiere, how many parents will be in the auditorium?"""
    # Define the number of girls and boys in the play
    num_girls = 6
    num_boys = 8

    # Calculate the total number of kids in the play
    total_kids = num_girls + num_boys

    # Calculate the total number of parents in the auditorium
    total_parents = total_kids * 2

    # Display the total number of parents
    result = total_parents
    return result

print(solution())