def solution():
    """Kobe and Pau went to a restaurant. Kobe ordered five pieces of fried chicken, and Pau ordered twice as much fried chicken as Kobe did. If they order another set of fried chicken, how many pieces of fried chicken will Pau have eaten in all?"""
    # Define the number of pieces of fried chicken Kobe ordered
    kobe_chicken = 5

    # Calculate the number of pieces of fried chicken Pau ordered
    pau_chicken = kobe_chicken * 2

    # Calculate the total number of pieces of fried chicken they will have eaten after ordering another set
    total_chicken = (kobe_chicken + pau_chicken) * 2

    # Display the total number of pieces of fried chicken Pau will have eaten in all
    result = pau_chicken + total_chicken
    return result

print(solution())