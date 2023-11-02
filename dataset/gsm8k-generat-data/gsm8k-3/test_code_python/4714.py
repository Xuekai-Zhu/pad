def solution():
    """Francine wants to know if a local chemical plant is releasing toxic waste that makes the frogs mutate. In one local pond, she catches 5 frogs with extra legs, 2 frogs with 2 heads, two frogs that are bright red, and 18 normal frogs. What percentage of the frogs have mutated, rounded to the nearest integer?"""
    # Calculate the total number of frogs
    total_frogs = 5 + 2 + 2 + 18

    # Calculate the total number of mutant frogs
    mutant_frogs = 5 + 2 + 2

    # Calculate the percentage of mutant frogs
    mutant_percentage = mutant_frogs / total_frogs * 100

    # Round the percentage to the nearest integer
    mutant_percentage = round(mutant_percentage)

    # Display the percentage of mutant frogs
    result = mutant_percentage
    return result

print(solution())