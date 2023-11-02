def solution():
    """Mary has 3 times as much candy as Megan. Mary then adds 10 more pieces of candy to her collection. If Megan has 5 pieces of candy, how many does Mary have in total?"""
    # Define the initial number of candy pieces that Megan has
    megan_candy = 5

    # Calculate the number of candy pieces that Mary has
    mary_candy = 3 * megan_candy + 10

    # Calculate the total number of candy pieces
    total_candy = megan_candy + mary_candy

    # return the result
    result = total_candy
    return result

print(solution())