def solution():
    box1_contacts = 50
    box1_price = 25

    box2_contacts = 99
    box2_price = 33

    # Calculate the price per contact for each box
    box1_ppc = box1_price / box1_contacts
    box2_ppc = box2_price / box2_contacts

    # Determine which box has the lower price per contact
    if box1_ppc < box2_ppc:
        chosen_box_ppc = box1_ppc
        chosen_box_contacts = box1_contacts
    else:
        chosen_box_ppc = box2_ppc
        chosen_box_contacts = box2_contacts

    # Calculate the number of contacts that equal $1 worth in the chosen box
    contacts_per_dollar = 1 / chosen_box_ppc
    result = contacts_per_dollar
    return result

print(solution())