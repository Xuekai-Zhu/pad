def solution():
    """A pharmacy is buying enough tubs for them to make their prescriptions this week. They already have 20 tubs left in storage but they need a total of 100 tubs for the week. Of the tubs they still need to buy, they buy a quarter from a new vendor then decide to go to their usual vendor for the rest. How many tubs is the pharmacy going to buy from the usual vendor?"""
    storage_tubs = 20
    total_tubs = 100
    new_vendor_tubs = (total_tubs - storage_tubs) / 4
    usual_vendor_tubs = total_tubs - storage_tubs - new_vendor_tubs
    result = usual_vendor_tubs
    return result

print(solution())