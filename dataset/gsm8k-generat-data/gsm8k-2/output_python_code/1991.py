def solution():
    """If 1 ounce of Dawn liquid soap can make 200,000 bubbles, and Dr. Bronner's liquid soap can make twice as many bubbles per ounce as Dawn liquid soap, then how many bubbles can be made from one half ounce of an equal mixture of Dawn and Dr. Bronner's liquid soaps?"""
    dawn_bubble_per_ounce = 200000
    bronner_bubble_per_ounce = 2 * dawn_bubble_per_ounce
    
    total_ounces = 0.5
    dawn_ounces = 0.25
    bronner_ounces = 0.25
    
    total_bubbles = (dawn_bubble_per_ounce * dawn_ounces) + (bronner_bubble_per_ounce * bronner_ounces)
    
    result = total_bubbles
    return result

print(solution())