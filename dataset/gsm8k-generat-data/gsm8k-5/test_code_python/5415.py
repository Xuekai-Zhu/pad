def solution():
    # Calculate the price per contact for the first box
    price_per_contact_1 = 25 / 50  # $25 for 50 contacts

    # Calculate the price per contact for the second box
    price_per_contact_2 = 33 / 99  # $33 for 99 contacts

    # Check which box has a lower price per contact
    if price_per_contact_1 < price_per_contact_2:
        # Buy the first box
        price_per_contact = price_per_contact_1
        contacts_per_dollar = 1 / price_per_contact
    else:
        # Buy the second box
        price_per_contact = price_per_contact_2
        contacts_per_dollar = 1 / price_per_contact

    result = contacts_per_dollar
    return result

print(solution())