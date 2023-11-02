def solution():
    """A snack machine accepts only quarters. Candy bars cost ¢25, each piece of chocolate costs ¢75, and a pack of juice costs ¢50. How many quarters are needed to buy three candy bars, two pieces of chocolate, and one pack of juice?"""
    candy_cost = 25 # in cents
    chocolate_cost = 75 # in cents
    juice_cost = 50 # in cents
    total_cost = (3 * candy_cost) + (2 * chocolate_cost) + juice_cost # in cents
    quarters_per_dollar = 4
    quarters_needed = total_cost // (quarters_per_dollar * 100)
    result = quarters_needed
    return result

print(solution())