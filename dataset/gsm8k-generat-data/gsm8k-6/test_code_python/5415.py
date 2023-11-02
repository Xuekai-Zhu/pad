def solution():
    # Calculate the cost per contact for each box
    cost_per_contact_box1 = 25/50  # cost per contact for box 1
    cost_per_contact_box2 = 33/99  # cost per contact for box 2

    # Choose the box with the lower cost per contact
    if cost_per_contact_box1 < cost_per_contact_box2:
        contacts_per_dollar = 50 / 25
    else:
        contacts_per_dollar = 99 / 33

    result = contacts_per_dollar
    return result

print(solution())