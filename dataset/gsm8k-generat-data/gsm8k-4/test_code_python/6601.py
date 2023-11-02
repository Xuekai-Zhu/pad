def solution():
    """Hakeem has always loved artichoke dip and plans to make it this weekend. He has $15 dollars to buy artichokes and can find the rest of the ingredients at home. It takes 3 artichokes to make 5 ounces of dip. How many ounces can he make if artichokes cost $1.25 each?"""
    # Define the cost of each artichoke and the total budget
    ARTICHOKE_COST = 1.25
    BUDGET = 15

    # Calculate the maximum number of artichokes Hakeem can buy with his budget
    num_artichokes = BUDGET / ARTICHOKE_COST

    # Calculate the number of ounces of dip Hakeem can make with the purchased artichokes
    num_ounces = (num_artichokes // 3) * 5

    # return the result
    result = num_ounces
    return result

print(solution())