def solution():
     starting_number_of_pencils = 20
     pencils_misplaced = 7
     pencils_broken = 3
     pencils_found = 4
     pencils_bought = 2
     pencils_left = starting_number_of_pencils - pencils_misplaced + pencils_found - pencils_broken + pencils_bought
     result = pencils_left
     return result

print(solution())