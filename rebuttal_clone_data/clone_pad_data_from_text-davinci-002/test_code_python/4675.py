def solution():
   total_pieces = 6 + 12 + (6 * 3)
   pieces_traded = 10
   knives_left = 6 - pieces_traded
   total_spoons = (6 * 3) + pieces_traded
   percent_knives = (knives_left / total_pieces) * 100
   result = percent_knives
   
   return result

print(solution())