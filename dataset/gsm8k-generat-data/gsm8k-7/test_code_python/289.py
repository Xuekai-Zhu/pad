def solution():
    total_models = 301
    
    # Let's assume the number of Chevys is x
    x = 0
    
    # We know that Jim has 3 more than twice the number of Fords than Chevys
    # So, let's assume the number of Fords is y
    y = x*2 + 3
    
    # We know Jim has 4 times as many Buicks as Fords
    # So, the number of Buicks is 4 times the number of Fords
    buicks = 4 * y
    
    # Finally, we know that the total number of models is the sum of Chevys, Fords, and Buicks
    # So, we can solve for x
    x = (total_models - buicks - y) / 2
    
    result = buicks
    return result

print(solution())