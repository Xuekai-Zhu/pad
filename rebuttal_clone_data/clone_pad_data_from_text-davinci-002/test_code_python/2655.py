def solution():
     total_decorations = 15
     sticky_strips = total_decorations
     thumbtacks = (total_decorations - sticky_strips) * (2/5)
     nails = (total_decorations - sticky_strips - thumbtacks) * (2/3)
     result = nails
     return result

print(solution())