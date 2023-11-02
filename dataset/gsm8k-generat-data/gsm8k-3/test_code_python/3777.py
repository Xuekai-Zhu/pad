def solution():
    """Janet has 60 less than four times as many siblings as Masud. Carlos has 3/4 times as many siblings as Masud. If Masud has 60 siblings, how many more siblings does Janet have more than Carlos?"""
    # Define the number of siblings Masud has
    masud_siblings = 60

    # Calculate the number of siblings Janet has
    janet_siblings = 4 * masud_siblings - 60

    # Calculate the number of siblings Carlos has
    carlos_siblings = 0.75 * masud_siblings

    # Calculate the difference between the number of siblings Janet and Carlos have
    difference = janet_siblings - carlos_siblings

    # Display the difference in the number of siblings Janet and Carlos have
    result = difference
    return result

print(solution())