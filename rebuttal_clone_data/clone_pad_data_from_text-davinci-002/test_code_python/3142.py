def solution():
     initial_oil = 4000
     oil_in_tanker = 3000
     capacity = 20000
     oil_needed = (capacity / 2) - (initial_oil + oil_in_tanker)
     result = oil_needed
     return result

print(solution())