def solution():
     tables = 20
     tablecloths = tables * 25
     place_settings = tables * 4 * 10
     centerpieces = tables * ((5 * 10) + (4 * 15))
     total_cost = tablecloths + place_settings + centerpieces
     result = total_cost
     return result

print(solution())