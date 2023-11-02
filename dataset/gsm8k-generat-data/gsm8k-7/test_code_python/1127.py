def solution():
    useful_percentage = 0.20
    valuable_percentage = 0.10
    junk_percentage = 0.70
    useful_items = 8

    # Calculate the total number of items in the attic
    total_items = useful_items / useful_percentage

    # Calculate the number of valuable heirlooms in the attic
    valuable_items = total_items * valuable_percentage

    # Calculate the number of junk items in the attic
    junk_items = total_items * junk_percentage

    # Calculate the number of junk items given that there are 8 useful items
    junk_items_given_useful = junk_items - (useful_items / useful_percentage)

    result = junk_items_given_useful
    return result

print(solution())