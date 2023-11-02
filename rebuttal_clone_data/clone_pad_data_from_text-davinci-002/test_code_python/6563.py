def solution():
     flower_plates = 4
     checked_plates = 8
     polka_dotted_plates = checked_plates * 2
     smashed_plates = 1
     total_plates = flower_plates + checked_plates + polka_dotted_plates - smashed_plates
     result = total_plates
     return result

print(solution())