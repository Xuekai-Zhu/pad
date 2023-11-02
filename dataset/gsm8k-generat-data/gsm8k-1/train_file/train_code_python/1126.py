def solution():
    """Mason is cleaning out all the junk in his attic. 20% of the items are useful, 10% are valuable heirlooms, and 70% are junk. If Marcus's attic has 8 useful items in it, how many junk items does it have?"""
    useful_percent = 20
    heirloom_percent = 10
    junk_percent = 70
    total_items = 100 # percent
    useful_items = 8
    useful_items_percent = useful_items / total_items * 100
    junk_items_percent = junk_percent + heirloom_percent + useful_percent - useful_items_percent
    junk_items = junk_items_percent / 100 * total_items
    result = junk_items
    return result

print(solution())