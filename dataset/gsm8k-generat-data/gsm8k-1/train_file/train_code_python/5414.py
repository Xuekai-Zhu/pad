def solution():
    """Adrian has the choice between two boxes of contacts. One has 50 contacts for $25, and the other has 99 contacts for $33. He chooses the box that costs less per individual contact. How many contacts will it take to equal $1 worth in whatever box he decides to buy?"""
    box1_price_per_contact = 25 / 50
    box2_price_per_contact = 33 / 99

    if box1_price_per_contact < box2_price_per_contact:
        price_per_contact = box1_price_per_contact
    else:
        price_per_contact = box2_price_per_contact

    contacts_per_dollar = 1 / price_per_contact
    result = contacts_per_dollar
    return result

print(solution())