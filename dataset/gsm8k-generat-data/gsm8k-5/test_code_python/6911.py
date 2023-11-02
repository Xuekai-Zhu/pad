def solution():
    # Calculate the number of tubs needed to meet the requirement for the week
    total_tubs_needed = 100
    tubs_in_storage = 20
    tubs_to_buy = total_tubs_needed - tubs_in_storage

    # Calculate the number of tubs to buy from the new vendor
    new_vendor_tubs = tubs_to_buy // 4

    # Calculate the number of tubs to buy from the usual vendor
    usual_vendor_tubs = tubs_to_buy - new_vendor_tubs

    result = usual_vendor_tubs
    return result

print(solution())