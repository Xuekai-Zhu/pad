def solution():
    """For her gift present, Lisa has saved $1200. She asks her mother, as well as her brother, to help her raise the total amount of money she needs to buy the gift. If her mother gave her 3/5 times of what she had saved and her brother gave her twice the amount her mother gave her, calculate the price of the gift she wanted to buy if she still had $400 less."""
    # Lisa saved $1200
    saved = 1200

    # Lisa's mother gave her 3/5 times of what she had saved
    mother_gave = 3/5 * saved

    # Lisa's brother gave her twice the amount her mother gave her
    brother_gave = 2 * mother_gave

    # Total amount Lisa has
    total = saved + mother_gave + brother_gave - 400

    # Price of the gift
    gift_price = total

    result = gift_price
    return result

print(solution())