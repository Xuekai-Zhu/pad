def solution():
    flower_plates = 4
    checked_plates = 8
    new_polka_plates = 2 * checked_plates
    total_plates = flower_plates + checked_plates + new_polka_plates
    total_plates -= 1  # Jack smashes one of the flowered plates
    result = total_plates
    return result

print(solution())