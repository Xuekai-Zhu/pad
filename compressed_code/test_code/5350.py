def solution():
    
    storage_tubs = 20
    total_tubs = 100
    new_vendor_tubs = (total_tubs - storage_tubs) / 4
    usual_vendor_tubs = total_tubs - storage_tubs - new_vendor_tubs
    result = usual_vendor_tubs
    return result

print(solution())