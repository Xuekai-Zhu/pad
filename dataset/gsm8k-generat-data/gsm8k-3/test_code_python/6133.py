def solution():
    """Jerry, Gabriel, and Jaxon ask their parents to buy them toys to play with. Jerry is bought 8 more toys than Gabriel, but Gabriel has twice as many toys as Jaxon. If Jaxon got 15 toys, what's the total number of toys they all have?"""
    # Define the number of toys Jaxon has
    jaxon_toys = 15

    # Calculate the number of toys Gabriel has
    gabriel_toys = jaxon_toys * 2

    # Calculate the number of toys Jerry has
    jerry_toys = gabriel_toys + 8

    # Calculate the total number of toys they have
    total_toys = jaxon_toys + gabriel_toys + jerry_toys

    # Display the total number of toys
    result = total_toys
    return result

print(solution())