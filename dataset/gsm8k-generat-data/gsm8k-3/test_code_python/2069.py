def solution():
    """Page collects fancy shoes and has 80 pairs in her closet.  She decides to donate 30% of her collection that she no longer wears.  After dropping off her donation, she treats herself and buys 6 more pairs to add to her collection.  How many shoes does she have now?"""
    # Define the initial number of shoes Page has
    initial_shoes = 80

    # Calculate the number of shoes she donates
    donated_shoes = initial_shoes * 0.3

    # Calculate the number of shoes she has left after donating
    remaining_shoes = initial_shoes - donated_shoes

    # Calculate the total number of shoes after buying 6 more
    total_shoes = remaining_shoes + 6

    # Display the total number of shoes
    result = total_shoes
    return result

print(solution())