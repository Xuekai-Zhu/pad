def solution():
    """At a restaurant, Juice Box A is 4 dollars. Juice Box B is 5 dollars more than Juice Box A. Juice Box C is 7 dollars more than Juice Box A. How much more is Juice box C than Juice Box B?"""
    juice_a = 4
    juice_b = juice_a + 5
    juice_c = juice_a + 7
    difference = juice_c - juice_b
    result = difference
    return result

print(solution())