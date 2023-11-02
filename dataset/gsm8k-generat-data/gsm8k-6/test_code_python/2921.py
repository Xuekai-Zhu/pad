def solution():
  total_rings = 52 # number of total rings

  # Let x be the number of times Martin rings the big bell
  x = total_rings / (1 + 4/3) # using the ratio of small to big bell rings
  
  result = x
  return result

print(solution())