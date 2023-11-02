def solution():
     turquoise_tile_cost = 13
     purple_tile_cost = 11
     wall1_area = 5 * 8
     wall2_area = 7 * 8
     total_area = wall1_area + wall2_area
     tiles_per_square_foot = 4
     total_tiles_needed = total_area * tiles_per_square_foot
     cost_of_turquoise_tiles = turquoise_tile_cost * total_tiles_needed
     cost_of_purple_tiles = purple_tile_cost * total_tiles_needed
     cost_savings = cost_of_turquoise_tiles - cost_of_purple_tiles
     result = cost_savings
 
     return result

print(solution())