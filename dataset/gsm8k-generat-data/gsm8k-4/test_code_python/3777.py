def solution():
    """Janet has 60 less than four times as many siblings as Masud. Carlos has 3/4 times as many siblings as Masud. If Masud has 60 siblings, how many more siblings does Janet have more than Carlos?"""
    # Define the number of siblings Masud has
    masud_siblings = 60

    # Define the number of siblings Carlos has
    carlos_siblings = 0.75 * masud_siblings

    # Define the number of siblings Janet has
    janet_siblings = (4 * masud_siblings) - 60

    # Calculate the difference between Janet's and Carlos's number of siblings
    difference = janet_siblings - carlos_siblings

    result = difference
    return result

print(solution())