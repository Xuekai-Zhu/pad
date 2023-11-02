def solution():
    allowance_per_week = 6  # Ryan's allowance is $6 each week
    chores_per_week = 3  # Ryan completes his chores for 3 weeks
    ice_cream_cones_cost = 1.25  # Ryan bought ice cream cones for himself and 3 friends
    total_allowance = allowance_per_week * chores_per_week * 3  # Ryan completes his chores for 3 weeks
    total_ice_cream_cones_cost = ice_cream_cones_cost * 3  # Ryan bought ice cream cones for himself and 3 friends
    total_friends_cost = ice_cream_cones_cost * 3  # Ryan bought 3 friends for himself and 3 friends
    total_cost = total_allowance + total_ice_cream_cones_cost + total_friends_cost  # Ryan wants to go to the movies and tickets cost $6.50 each

print(solution())