def solution():
    """Greg has lent his sister Tessa money on several occasions. Greg writes down all of his sister's debts in a notebook, the first time he lent her $40. A week later, Tessa paid him back half of her debt. A few days later she asked him for $10 more. How much does Tessa still owe Greg?"""
    # Define the initial debt
    debt = 40

    # Calculate the amount Tessa paid back
    paid_back = debt / 2

    # Subtract the amount paid back
    debt -= paid_back

    # Add the extra $10 Tessa borrowed
    debt += 10

    # Return the remaining debt
    result = debt
    return result

print(solution())