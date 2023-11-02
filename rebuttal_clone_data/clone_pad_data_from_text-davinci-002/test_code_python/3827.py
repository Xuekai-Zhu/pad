def solution():
     Jericho_money = 60
     Annika_owed = 14
     Manny_owed = Jericho_money / 2
     Total_owed = Annika_owed + Manny_owed
     Jericho_leftover = Jericho_money - Total_owed
     result = Jericho_leftover
     return result

print(solution())