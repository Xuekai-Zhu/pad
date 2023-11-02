def solution():
    
    num_classes = 5
    whiteboards_per_class = 2
    ink_per_whiteboard = 20 
    ink_price_per_ml = 0.5 
    total_ink = num_classes * whiteboards_per_class * ink_per_whiteboard
    total_cost = total_ink * ink_price_per_ml
    result = total_cost
    return result

print(solution())