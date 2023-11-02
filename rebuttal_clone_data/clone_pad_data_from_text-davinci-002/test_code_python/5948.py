def solution():
     land_cost = 50
     brick_cost = 100
     roof_tile_cost = 10
     square_meters_required = 2000
     bricks_required = 10000
     roof_tiles_required = 500
     land_total_cost = land_cost * square_meters_required
     brick_total_cost = brick_cost * (bricks_required / 1000)
     roof_tile_total_cost = roof_tile_cost * roof_tiles_required
     total_cost = land_total_cost + brick_total_cost + roof_tile_total_cost
     result = total_cost
     return result

print(solution())