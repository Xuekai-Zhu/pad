def solution():
    sharpening_frequency = 5  # Jenine can sharpen a pencil 5 times before it runs out
    use_duration = 1.5  # Jenine needs to sharpen a pencil every 1.5 hours of use
    hours_needed = 105  # Jenine needs to write for 105 hours
    pencils_owned = 10  # Jenine already has 10 pencils
    hours_per_pencil = sharpening_frequency * use_duration  # Calculate the total use hours per pencil
    pencils_needed = (hours_needed / hours_per_pencil) - pencils_owned  # Calculate the number of additional pencils needed
    cost_per_pencil = 2  # Each new pencil costs $2
    total_cost = pencils_needed * cost_per_pencil  # Calculate the total cost of the additional pencils needed
    result = total_cost
    return result

print(solution())