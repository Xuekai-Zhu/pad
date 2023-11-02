def solution():
    num_dog_treats = 8
    num_chew_toys = 2
    num_rawhide_bones = 10
    num_credit_cards = 4

    # Calculate the total number of items Bailey purchased
    total_items = num_dog_treats + num_chew_toys + num_rawhide_bones

    # Calculate the number of items in each credit card charge
    items_per_charge = total_items / num_credit_cards
    result = items_per_charge
    return result

print(solution())