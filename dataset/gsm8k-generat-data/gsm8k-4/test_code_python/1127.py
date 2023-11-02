def solution():
    """Mason is cleaning out all the junk in his attic. 20% of the items are useful, 10% are valuable heirlooms, and 70% are junk. If Marcus's attic has 8 useful items in it, how many junk items does it have?"""
    # Define the percentage of useful, heirloom, and junk items in the attic
    useful_percentage = 0.2
    heirloom_percentage = 0.1
    junk_percentage = 0.7

    # Define the number of useful items in the attic
    useful_items = 8

    # Calculate the total number of items in the attic
    total_items = useful_items / useful_percentage

    # Calculate the number of heirloom items in the attic
    heirloom_items = total_items * heirloom_percentage

    # Calculate the number of junk items in the attic
    junk_items = total_items * junk_percentage

    # Calculate the total number of items in the attic
    total_items = useful_items + heirloom_items + junk_items

    # Calculate the number of junk items in the attic
    junk_items = total_items * junk_percentage

    # Return the result
    result = junk_items
    return result

print(solution())