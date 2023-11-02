def solution():
    
    dawn_bubble_per_ounce = 200000
    bronner_bubble_per_ounce = 2 * dawn_bubble_per_ounce
    
    total_ounces = 0.5
    dawn_ounces = 0.25
    bronner_ounces = 0.25
    
    total_bubbles = (dawn_bubble_per_ounce * dawn_ounces) + (bronner_bubble_per_ounce * bronner_ounces)
    
    result = total_bubbles
    return result

print(solution())