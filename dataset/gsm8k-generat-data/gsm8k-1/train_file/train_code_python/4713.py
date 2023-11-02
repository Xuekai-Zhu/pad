def solution():
    """Francine wants to know if a local chemical plant is releasing toxic waste that makes the frogs mutate. In one local pond, she catches 5 frogs with extra legs, 2 frogs with 2 heads, two frogs that are bright red, and 18 normal frogs. What percentage of the frogs have mutated, rounded to the nearest integer?"""
    total_frogs = 27
    mutated_frogs = 5 + 2 + 2
    percent_mutated = round((mutated_frogs / total_frogs) * 100)
    result = percent_mutated
    return result

print(solution())