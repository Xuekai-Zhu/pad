def solution():
    """Mason is cleaning out all the junk in his attic. 20% of the items are useful, 10% are valuable heirlooms, and 70% are junk. If Marcus's attic has 8 useful items in it, how many junk items does it have?"""
    # Define the percentage of useful items and valuable heirlooms
    USEFUL_PERCENTAGE = 20
    HEIRLOOM_PERCENTAGE = 10

    # Define the number of useful items in the attic
    useful_items = 8

    # Calculate the total percentage of non-junk items
    non_junk_percentage = USEFUL_PERCENTAGE + HEIRLOOM_PERCENTAGE

    # Calculate the total percentage of junk items
    junk_percentage = 100 - non_junk_percentage

    # Calculate the total number of items in the attic
    total_items = useful_items / (USEFUL_PERCENTAGE / 100)

    # Calculate the number of junk items in the attic
    junk_items = total_items - (useful_items + (total_items * (HEIRLOOM_PERCENTAGE / 100)))

    # Display the number of junk items
    result = junk_items
    return result

print(solution())