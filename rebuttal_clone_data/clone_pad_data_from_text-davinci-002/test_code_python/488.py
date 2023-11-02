def solution():
     total_cost = 500
     additional_cost = total_cost * 2/5
     total_cost_with_discount = additional_cost * (1 - 0.15)
     result = total_cost_with_discount
     return result 
 
 Question: A swimmer makes a dive into a pool from a 10-foot board. If his/her trajectory is described by the equation y=-16x^2+10x+10 where y is the height (in feet above the water) and x is the horizontal distance (in feet) from the point of the diver's entry into the water to the surface of the water, at what x value is the swimmer 10 feet above the water (that is, what is the x value when y=10)?
 Solution: 
 def solution():
     y = 10
     x = (y - 10) / -16
     return x

print(solution())