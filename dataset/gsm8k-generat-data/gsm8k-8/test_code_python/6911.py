def solution():
    # Define the number of tubs already in storage and the total number needed for the week
    storage_tubs = 20
    total_tubs = 100

    # Calculate the number of tubs still needed
    still_needed = total_tubs - storage_tubs

    # Calculate the number of tubs to buy from the new vendor
    new_vendor_tubs = still_needed * 0.25

    # Calculate the number of tubs to buy from the usual vendor
    usual_vendor_tubs = still_needed - new_vendor_tubs
    result = usual_vendor_tubs
    return result

print(solution())