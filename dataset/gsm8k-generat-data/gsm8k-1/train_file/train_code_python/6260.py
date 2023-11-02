def solution():
    """At the same store, Peter bought 2 pairs of pants and 5 shirts for $62 total, and Jessica bought 2 shirts for $20 total. Each pair of pants cost the same price, and each shirt cost the same price. How much does 1 pair of pants cost?"""
    pants_cost = (62 - 5 * (20/2)) / 2
    result = pants_cost
    return result

print(solution())