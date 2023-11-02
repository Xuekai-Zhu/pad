def solution():
    """Mary has 3 times as much candy as Megan. Mary then adds 10 more pieces of candy to her collection. If Megan has 5 pieces of candy, how many does Mary have in total?"""
    # Define the number of pieces of candy Megan has
    megan_candy = 5

    # Calculate the number of pieces of candy Mary has
    mary_candy = 3 * megan_candy + 10

    # Calculate the total number of pieces of candy
    total_candy = megan_candy + mary_candy

    # Display the total number of pieces of candy
    result = total_candy
    return result

print(solution())