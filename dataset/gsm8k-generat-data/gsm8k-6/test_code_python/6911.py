def solution():
    # Calculate the number of tubs the pharmacy needs to buy
    total_tubs_needed = 100
    tubs_already_in_storage = 20
    tubs_needed = total_tubs_needed - tubs_already_in_storage

    # Calculate the number of tubs to buy from the new vendor
    new_vendor_tubs = tubs_needed // 4

    # Calculate the number of tubs to buy from the usual vendor
    usual_vendor_tubs = tubs_needed - new_vendor_tubs

    result = usual_vendor_tubs
    return result

print(solution())