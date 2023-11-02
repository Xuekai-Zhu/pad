def solution():
    
    flower_plates = 4
    checked_plates = 8
    polka_dotted_plates = 2 * checked_plates
    total_plates = flower_plates + checked_plates + polka_dotted_plates - 1
    result = total_plates
    return result

print(solution())