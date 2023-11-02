def solution():
    """Adrian has the choice between two boxes of contacts. One has 50 contacts for $25, and the other has 99 contacts for $33.
    He chooses the box that costs less per individual contact. How many contacts will it take to equal $1 worth in whatever box he decides to buy?"""
    # Define the prices and number of contacts in each box
    box1_price = 25
    box1_contacts = 50
    box2_price = 33
    box2_contacts = 99

    # Calculate the price per contact for each box
    box1_price_per_contact = box1_price / box1_contacts
    box2_price_per_contact = box2_price / box2_contacts

    # Choose the box with the lower price per contact
    if box1_price_per_contact < box2_price_per_contact:
        price_per_contact = box1_price_per_contact
        contacts_per_dollar = 1 / price_per_contact
    else:
        price_per_contact = box2_price_per_contact
        contacts_per_dollar = 1 / price_per_contact

    result = round(contacts_per_dollar)
    return result

print(solution())