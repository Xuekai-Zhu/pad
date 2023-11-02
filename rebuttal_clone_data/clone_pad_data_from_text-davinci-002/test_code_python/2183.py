def solution():
     bedroom = 8
     living_room = 20
     kitchen = 11
     guest_bedroom = bedroom - 2
     hallway = 4
     ruined_bedroom = 3
     ruined_guest_bedroom = ruined_bedroom - 1
     leftover = 6
     total = (bedroom + living_room + kitchen + guest_bedroom + hallway) - (ruined_bedroom + ruined_guest_bedroom) + leftover
     result = total
     return result

print(solution())