def solution():
    """Bailey needs to buy 2 new sets of towels for the guest bathroom and 4 new sets for her master bathroom.  The set of towels for the guest bathroom are $40.00 each and the master bathroom set is $50.00 each.  The store is currently offering 20% off so how much will Bailey spend on towel sets?"""
    # Define the cost of each type of towel set and the discount percentage
    GUEST_TOWEL_SET_PRICE = 40
    MASTER_TOWEL_SET_PRICE = 50
    DISCOUNT_PERCENTAGE = 0.2

    # Define the number of towel sets Bailey needs to buy for each bathroom
    guest_towel_sets = 2
    master_towel_sets = 4

    # Calculate the regular cost of the towel sets
    guest_towel_sets_cost = guest_towel_sets * GUEST_TOWEL_SET_PRICE
    master_towel_sets_cost = master_towel_sets * MASTER_TOWEL_SET_PRICE
    total_cost = guest_towel_sets_cost + master_towel_sets_cost

    # Calculate the discount amount
    discount_amount = total_cost * DISCOUNT_PERCENTAGE

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost - discount_amount

    # Display the total cost after the discount
    result = total_cost_after_discount
    return result

print(solution())