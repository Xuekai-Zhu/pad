def solution():
     dvds = 8
     blu_rays = 4
     cost_dvds = 12
     cost_blu_ray = 18
     total_movies = dvds + blu_rays
     total_cost = (dvds * cost_dvds) + (blu_rays * cost_blu_ray)
     average_cost = total_cost / total_movies
     
     return average_cost

print(solution())