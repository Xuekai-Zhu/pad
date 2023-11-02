def solution():
    """Kobe and Pau went to a restaurant. Kobe ordered five pieces of fried chicken, and Pau ordered twice as much fried chicken as Kobe did. If they order another set of fried chicken, how many pieces of fried chicken will Pau have eaten in all?"""
    # Define the initial number of chicken pieces
    kobe_chicken = 5
    pau_chicken = 2 * kobe_chicken

    # Add another set of fried chicken
    kobe_chicken += 5
    pau_chicken += 5 * 2

    # Calculate the total number of chicken pieces Pau ate
    total_pau_chicken = pau_chicken

    # Return the result
    result = total_pau_chicken
    return result

print(solution())