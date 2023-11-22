def solution():
    
    # Define the ratio of popsicles Betty and Sam have
    ratio = 5/6

    # Calculate the total number of popsicles they have together
    total_popsicles = 165

    # Calculate the number of popsicles Betty has
    betty_popsicles = total_popsicles / (5 + 6)

    # Calculate the number of popsicles Sam has
    sam_popsicles = total_popsicles - betty_popsicles

    # Calculate the difference in popsicles between Sam and Betty
    difference = sam_popsicles - betty_popsicles

    # Display the difference in popsicles between Sam and Betty
    result = difference
    return result

print(solution())