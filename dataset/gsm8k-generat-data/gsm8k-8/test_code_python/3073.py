def solution():
    # Define the number of items Bailey bought
    dog_treats = 8
    chew_toys = 2
    rawhide_bones = 10

    # Calculate the total number of items
    total_items = dog_treats + chew_toys + rawhide_bones

    # Calculate the number of items per credit card
    items_per_card = total_items / 4

    result = items_per_card
    return result

print(solution())