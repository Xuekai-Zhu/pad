def solution():
     pencils_bought = 30
     pencils_lost = 6
     pencils_remaining = pencils_bought - pencils_lost
     pencils_lost_2 = pencils_remaining / 3
     pencils_currently = pencils_remaining - pencils_lost_2
     result = pencils_currently
     return result

print(solution())