def solution():
     total_miles = 16
     miles_paved_1 = 4
     miles_paved_2 = (2 * miles_paved_1) - 1
     miles_paved_3 = total_miles - (miles_paved_1 + miles_paved_2)
     barrels_pitch = (3 * miles_paved_3) / 5
     result = barrels_pitch
     return result

print(solution())