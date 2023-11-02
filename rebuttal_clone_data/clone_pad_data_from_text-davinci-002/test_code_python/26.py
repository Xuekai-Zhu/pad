def solution():
     """Jack is stranded on a desert island. He wants some salt to season his fish. He collects 2 liters of seawater in an old bucket. If the water is 20% salt, how many ml of salt will Jack get when all the water evaporates?"""
     seawater_collected = 2
     salt_percentage = 20
     salt_total = (seawater_collected * salt_percentage) / 100
     result = salt_total
     return result

print(solution())