def solution():
    """A pharmacy is buying enough tubs for them to make their prescriptions this week. They already have 20 tubs left in storage but they need a total of 100 tubs for the week. Of the tubs they still need to buy, they buy a quarter from a new vendor then decide to go to their usual vendor for the rest. How many tubs is the pharmacy going to buy from the usual vendor?"""
    total_tubs = 100
    tubs_in_storage = 20
    tubs_to_buy = total_tubs - tubs_in_storage
    tubs_from_new_vendor = tubs_to_buy / 4
    tubs_from_usual_vendor = tubs_to_buy - tubs_from_new_vendor
    result = tubs_from_usual_vendor
    return result

print(solution())