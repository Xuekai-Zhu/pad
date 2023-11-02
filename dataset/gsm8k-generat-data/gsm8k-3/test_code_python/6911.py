def solution():
    """A pharmacy is buying enough tubs for them to make their prescriptions this week. They already have 20 tubs left in storage but they need a total of 100 tubs for the week. Of the tubs they still need to buy, they buy a quarter from a new vendor then decide to go to their usual vendor for the rest. How many tubs is the pharmacy going to buy from the usual vendor?"""
    # Define the number of tubs already in storage and the total number of tubs needed
    TUBS_IN_STORAGE = 20
    TOTAL_TUBS = 100

    # Calculate the number of tubs the pharmacy needs to buy
    tubs_to_buy = TOTAL_TUBS - TUBS_IN_STORAGE

    # Calculate the number of tubs the pharmacy buys from the new vendor
    new_vendor_tubs = tubs_to_buy // 4

    # Calculate the number of tubs the pharmacy buys from the usual vendor
    usual_vendor_tubs = tubs_to_buy - new_vendor_tubs

    # Display the number of tubs the pharmacy buys from the usual vendor
    result = usual_vendor_tubs
    return result

print(solution())