def solution():
    """Two tribes of soldiers gathered for a battle. The number of women was double the number of cannoneers. There were 63 cannoneers.  None of the cannoneers were women.  The total number of men is twice the number of women.  How many people in total are there?"""
    # Define the number of cannoneers and women
    cannoneers = 63
    women = cannoneers * 2

    # Define the number of men
    men = women * 2

    # Calculate the total number of soldiers
    total_soldiers = cannoneers + women + men

    # Return the result
    result = total_soldiers
    return result

print(solution())