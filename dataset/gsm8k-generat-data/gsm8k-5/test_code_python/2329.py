def solution():
    dosage_per_day = 3  # Archie needs to take the antibiotic three times a day
    cost_per_dosage = 3  # Each dosage of antibiotic costs $3
    days_per_week = 7  # Archie needs to take the antibiotic for a week

    # Calculate the total cost of antibiotics for a week
    total_cost = dosage_per_day * cost_per_dosage * days_per_week
    result = total_cost
    return result

print(solution())