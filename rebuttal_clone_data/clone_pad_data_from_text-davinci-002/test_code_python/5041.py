def solution():
     total_square_feet = 200
     square_feet_of_3_paintings = 3 * 5 * 5
     square_feet_of_1_painting = 10 * 8
     square_feet_of_final_painting = 5 * 5
     final_painting_width = (total_square_feet - square_feet_of_3_paintings - square_feet_of_1_painting) / 5
     
     return final_painting_width

print(solution())