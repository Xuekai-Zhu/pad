def solution():
    """
    For her gift present, Lisa has saved $1200. She asks her mother, as well as her brother, to help her raise the total amount of money she needs to buy the gift.
    If her mother gave her 3/5 times of what she had saved and her brother gave her twice the amount her mother gave her, calculate the price of the gift she wanted to buy if she still had $400 less.
    """
    lisa_savings = 1200
    mother_contribution = (3/5) * lisa_savings
    brother_contribution = 2 * mother_contribution
    total_money_raised = lisa_savings + mother_contribution + brother_contribution - 400
    result = total_money_raised
    return result

print(solution())