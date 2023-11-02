def solution():
    is_service_dog = True
    is_drug_detection = False
    special_travel_accommodations = True
    if is_service_dog and not is_drug_detection and special_travel_accommodations:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())