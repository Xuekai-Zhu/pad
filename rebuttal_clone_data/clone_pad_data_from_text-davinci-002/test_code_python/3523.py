def solution():
     total_students = 200
     percent_female = 60
     percent_brunette_female = 50
     percent_under_5_feet = 50
     total_female_students = total_students * (percent_female / 100)
     total_brunette_female_students = total_female_students * (percent_brunette_female / 100)
     total_under_5_feet_students = total_brunette_female_students * (percent_under_5_feet / 100)
     result = total_under_5_feet_students
     
     return result

print(solution())