def solution():
    """Adrian has the choice between two boxes of contacts.  One has 50 contacts for $25, and the other has 99 contacts for $33. He chooses the box that costs less per individual contact.  How many contacts will it take to equal $1 worth in whatever box he decides to buy?"""
    # Calculate the cost per contact for each box
    box1_cost_per_contact = 25 / 50
    box2_cost_per_contact = 33 / 99

    # Determine which box has the lower cost per contact
    if box1_cost_per_contact < box2_cost_per_contact:
        chosen_box_cost_per_contact = box1_cost_per_contact
    else:
        chosen_box_cost_per_contact = box2_cost_per_contact

    # Calculate the number of contacts that equal $1 in the chosen box
    contacts_per_dollar = 1 / chosen_box_cost_per_contact

    # Display the number of contacts per dollar in the chosen box
    result = contacts_per_dollar
    return result

print(solution())