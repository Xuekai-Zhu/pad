def solution():
    """Mason is cleaning out all the junk in his attic. 20% of the items are useful, 10% are valuable heirlooms, and 70% are junk. If Marcus's attic has 8 useful items in it, how many junk items does it have?"""
    useful_items_percentage = 0.2
    valuable_items_percentage = 0.1
    junk_items_percentage = 0.7
    useful_items = 8
    total_items = useful_items / useful_items_percentage
    valuable_items = total_items * valuable_items_percentage
    junk_items = total_items * junk_items_percentage
    junk_items -= valuable_items
    junk_items -= useful_items
    result = junk_items
    return result

print(solution())