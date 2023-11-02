def solution():
    # Calculate the cost per contact in each box
    cost_per_contact_box1 = 25 / 50
    cost_per_contact_box2 = 33 / 99

    # Determine which box has the lower cost per contact
    if cost_per_contact_box1 < cost_per_contact_box2:
        chosen_box_cost = 25
        chosen_box_contacts = 50
    else:
        chosen_box_cost = 33
        chosen_box_contacts = 99

    # Calculate how many contacts equal $1 in the chosen box
    contacts_per_dollar = chosen_box_contacts / chosen_box_cost
    result = contacts_per_dollar
    return result

print(solution())