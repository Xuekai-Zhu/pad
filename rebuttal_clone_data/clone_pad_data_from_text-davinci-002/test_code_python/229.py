def solution():
     """Jan buys 1000 feet of cable. She splits it up into 25-foot sections. She gives 1/4 of that to a friend. She then puts half of the rest in storage. How much does she keep on hand?"""
     cable_bought = 1000
     cable_sections = cable_bought / 25
     cable_given = cable_sections / 4
     cable_kept = cable_sections - cable_given
     result = cable_kept
     return result

print(solution())