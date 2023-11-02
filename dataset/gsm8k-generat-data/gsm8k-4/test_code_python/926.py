def solution():
    """Bailey needs to buy 2 new sets of towels for the guest bathroom and 4 new sets for her master bathroom. The set of towels for the guest bathroom are $40.00 each and the master bathroom set is $50.00 each. The store is currently offering 20% off so how much will Bailey spend on towel sets?"""
    # Define the number of towel sets needed
    guest_bathroom = 2
    master_bathroom = 4

    # Define the prices of each towel set
    guest_price = 40.0
    master_price = 50.0

    # Calculate the total cost before discount
    total_cost = (guest_bathroom * guest_price) + (master_bathroom * master_price)

    # Calculate the discount amount
    discount = total_cost * 0.2

    # Calculate the total cost after discount
    total_cost -= discount

    # return the result
    result = total_cost
    return result

print(solution())