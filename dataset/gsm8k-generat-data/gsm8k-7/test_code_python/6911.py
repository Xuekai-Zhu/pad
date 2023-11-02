def solution():
    num_tubs_in_storage = 20
    total_num_tubs = 100
    num_tubs_from_new_vendor = (total_num_tubs - num_tubs_in_storage) / 4
    num_tubs_from_usual_vendor = total_num_tubs - num_tubs_in_storage - num_tubs_from_new_vendor
    result = num_tubs_from_usual_vendor
    return result

print(solution())