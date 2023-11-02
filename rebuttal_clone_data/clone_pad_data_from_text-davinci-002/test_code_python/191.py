def solution():
     """In a section of the forest, there are 100 weasels and 50 rabbits. Three foxes invade this region and hunt the rodents. Each fox catches an average of 4 weasels and 2 rabbits per week. How many rabbits and weasels will be left after 3 weeks?"""
     weasels = 100
     rabbits = 50
     foxes = 3
     weasel_catch = 4
     rabbit_catch = 2
     weeks = 3
     weasel_loss = foxes * weasel_catch * weeks
     rabbit_loss = foxes * rabbit_catch * weeks
     weasels_left = weasels - weasel_loss
     rabbits_left = rabbits - rabbit_loss
     result = "%d weasels and %d rabbits will be left after 3 weeks." % (weasels_left, rabbits_left)
     return result

print(solution())