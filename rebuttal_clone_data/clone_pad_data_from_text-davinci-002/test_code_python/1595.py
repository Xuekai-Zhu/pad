def solution():
     three_point_basket = 3
     two_point_basket = 2
     fireflies_three_point_baskets = 7
     hornets_two_point_baskets = 2
     fireflies_points = fireflies_three_point_baskets * three_point_basket
     hornets_points = hornets_two_point_baskets * two_point_basket
     total_points = fireflies_points + hornets_points
     fireflies_total_points = total_points - hornets_points
     result = fireflies_total_points
     return result

print(solution())