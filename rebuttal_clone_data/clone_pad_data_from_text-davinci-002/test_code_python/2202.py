def solution():
     classes = 5
     whiteboards_per_class = 2
     ink_per_whiteboard = 20
     cost_per_ml = 0.5
     total_cost = classes * whiteboards_per_class * ink_per_whiteboard * cost_per_ml
     result = total_cost
     return result

print(solution())