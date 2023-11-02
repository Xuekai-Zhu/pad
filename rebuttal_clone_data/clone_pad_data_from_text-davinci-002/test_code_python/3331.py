def solution():
    total_plates = 38
    weight_of_plates = 10
    weight_limit = 20
    plates_to_remove = total_plates - weight_limit/weight_of_plates
    return plates_to_remove

print(solution())