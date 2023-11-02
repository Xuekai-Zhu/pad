def solution():
    """Francine wants to know if a local chemical plant is releasing toxic waste that makes the frogs mutate. In one local pond, she catches 5 frogs with extra legs, 2 frogs with 2 heads, two frogs that are bright red, and 18 normal frogs. What percentage of the frogs have mutated, rounded to the nearest integer?"""
    # Define the total number of frogs
    total_frogs = 27

    # Calculate the number of mutated frogs
    mutated_frogs = 5 + 2 + 2

    # Calculate the percentage of mutated frogs
    percentage_mutated = (mutated_frogs / total_frogs) * 100

    # Round the percentage to the nearest integer
    rounded_percentage = round(percentage_mutated)

    # Return the result
    result = rounded_percentage
    return result

print(solution())