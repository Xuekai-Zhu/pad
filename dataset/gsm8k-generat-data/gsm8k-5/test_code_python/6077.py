def solution():
    red_roses_per_dozen = 12  # There are 12 roses in a dozen
    total_red_roses = 2 * red_roses_per_dozen  # Jezebel needs 2 dozens of red roses
    cost_per_red_rose = 1.50  # Each red rose costs $1.50
    total_cost_red_roses = total_red_roses * cost_per_red_rose  # Calculate the total cost of red roses

    num_sunflowers = 3  # Jezebel needs 3 sunflowers
    cost_per_sunflower = 3  # Each sunflower costs $3
    total_cost_sunflowers = num_sunflowers * cost_per_sunflower  # Calculate the total cost of sunflowers

    # Calculate the total cost of all the flowers
    total_cost = total_cost_red_roses + total_cost_sunflowers
    result = total_cost
    return result

print(solution())