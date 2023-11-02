def solution():
     bonnets_on_monday = 10
     bonnets_on_tuesday = 2 * bonnets_on_monday
     bonnets_on_wednesday = 2 * bonnets_on_monday
     bonnets_on_thursday = 5 + bonnets_on_monday
     bonnets_on_friday = 5 - bonnets_on_monday
     
     total_bonnets = (bonnets_on_monday + bonnets_on_tuesday + bonnets_on_wednesday + bonnets_on_thursday + bonnets_on_friday) / 5 
     return total_bonnets

print(solution())