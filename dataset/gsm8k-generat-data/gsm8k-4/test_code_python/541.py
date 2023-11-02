def solution():
    """Tonya is buying Christmas gifts for her sisters. She has 2 sisters and wants to spend the exact same amount on each. She buys her younger sister 4 dolls that cost $15 each. She plans to buy lego sets for her older sister. They cost $20 each. How many lego sets does she buy?"""
    # Calculate the total amount spent on the younger sister's gifts
    younger_sister_gifts = 4 * 15

    # Calculate the amount that Tonya has left to spend on the older sister's gifts
    older_sister_budget = (2 * younger_sister_gifts) / 2 - younger_sister_gifts

    # Calculate the number of lego sets that Tonya can buy with the remaining budget
    lego_sets = older_sister_budget / 20

    result = lego_sets
    return result

print(solution())