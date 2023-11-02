def solution():
    dawn_bubbles_per_ounce = 200000
    dr_bronner_bubbles_per_ounce = 2 * dawn_bubbles_per_ounce
    total_bubbles_per_ounce = dawn_bubbles_per_ounce + dr_bronner_bubbles_per_ounce
    half_ounce = 0.5

    # Calculate the total bubbles made from half an ounce of the mixture
    total_bubbles = total_bubbles_per_ounce * half_ounce
    result = total_bubbles
    return result

print(solution())