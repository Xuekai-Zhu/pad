def solution():
    # Calculate the number of bubbles made from one half ounce of equal mixture of Dawn and Dr. Bronner's liquid soaps
    bubbles_per_ounce_Dawn = 200000
    bubbles_per_ounce_Bronner = 2 * bubbles_per_ounce_Dawn
    total_bubbles_per_ounce = bubbles_per_ounce_Dawn + bubbles_per_ounce_Bronner
    total_bubbles_half_ounce = total_bubbles_per_ounce * 0.5
    result = total_bubbles_half_ounce
    return result

print(solution())