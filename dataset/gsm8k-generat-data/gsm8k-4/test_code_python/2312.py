def solution():
    """For her gift present, Lisa has saved $1200. She asks her mother, as well as her brother, to help her raise the total amount of money she needs to buy the gift. If her mother gave her 3/5 times of what she had saved and her brother gave her twice the amount her mother gave her, calculate the price of the gift she wanted to buy if she still had $400 less."""
    # Define the initial amount saved by Lisa
    initial_amount = 1200

    # Calculate the amount given by Lisa's mother
    mother_amount = initial_amount * 0.6

    # Calculate the amount given by Lisa's brother
    brother_amount = mother_amount * 2

    # Calculate the total amount raised
    total_amount = initial_amount + mother_amount + brother_amount - 400

    # Display the price of the gift that Lisa wanted to buy
    result = total_amount
    return result

print(solution())