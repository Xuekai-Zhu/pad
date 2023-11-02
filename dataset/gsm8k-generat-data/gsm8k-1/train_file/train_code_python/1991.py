def solution():
    """If 1 ounce of Dawn liquid soap can make 200,000 bubbles, and Dr. Bronner's liquid soap can make twice as many bubbles per ounce as Dawn liquid soap, then how many bubbles can be made from one half ounce of an equal mixture of Dawn and Dr. Bronner's liquid soaps?"""
    dawn_bubbles_per_oz = 200000
    bronner_bubbles_per_oz = 2 * dawn_bubbles_per_oz
    half_oz_total_bubbles = (dawn_bubbles_per_oz + bronner_bubbles_per_oz) * 0.5
    result = half_oz_total_bubbles
    return result

print(solution())