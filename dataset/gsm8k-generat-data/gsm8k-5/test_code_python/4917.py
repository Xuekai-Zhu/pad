def solution():
    fish_weight = 540  # Lizzy has to ship 540 pounds of fish
    crate_weight = 30  # Each crate can hold 30 pounds of fish
    num_crates = fish_weight // crate_weight  # Calculate the number of crates needed
    if fish_weight % crate_weight != 0:  # Add an extra crate if there is any leftover fish
        num_crates += 1
    crate_cost = 1.5  # Each crate costs $1.5 to ship
    total_cost = num_crates * crate_cost  # Calculate the total cost of shipping
    result = total_cost
    return result

print(solution())