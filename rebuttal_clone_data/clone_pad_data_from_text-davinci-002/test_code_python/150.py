def solution():
     """Angela is a bike messenger in New York. She needs to deliver 8 times as many packages as meals. If she needs to deliver 27 meals and packages combined, how many meals does she deliver?"""
     meals = 8
     packages = 1
     total = 27
     result = (total - meals) / packages
     return result

print(solution())