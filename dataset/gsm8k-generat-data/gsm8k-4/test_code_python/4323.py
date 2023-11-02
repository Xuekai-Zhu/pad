def solution():
    """Sandra's dog gave birth to 7 puppies. Her vet gave her 105 portions of formula to give to the puppies for 5 days. How many times a day should Sandra feed the puppies?"""
    # Define the number of puppies and portions of formula
    num_puppies = 7
    num_formula_portions = 105

    # Calculate the total amount of formula needed for all the puppies
    total_formula = num_puppies * num_formula_portions

    # Calculate the number of times Sandra should feed the puppies per day
    feedings_per_day = total_formula / (5 * num_puppies)

    # Round up to the nearest whole number for practical purposes
    feedings_per_day = int(feedings_per_day + 0.5)

    result = feedings_per_day
    return result

print(solution())