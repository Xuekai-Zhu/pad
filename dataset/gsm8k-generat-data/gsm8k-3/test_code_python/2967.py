def solution():
    """Dave weighs 175 pounds and can bench press three times his body weight.  
    Craig can only bench press 20% of the amount Dave can.  Mark is new and can bench press 50 pounds less than Craig.  
    How much can Mark bench press?"""
    
    # Define Dave's weight and bench press ratio
    dave_weight = 175
    dave_ratio = 3
    
    # Calculate Dave's bench press weight
    dave_bench_press = dave_weight * dave_ratio
    
    # Calculate Craig's bench press weight
    craig_ratio = 0.2
    craig_bench_press = dave_bench_press * craig_ratio
    
    # Calculate Mark's bench press weight
    mark_bench_press = craig_bench_press - 50
    
    # Display Mark's bench press weight
    result = mark_bench_press
    return result

print(solution())