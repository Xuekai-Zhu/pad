def solution():
    """Greg has lent his sister Tessa money on several occasions. Greg writes down all of his sister's debts in a notebook, the first time he lent her $40. A week later, Tessa paid him back half of her debt. A few days later she asked him for $10 more. How much does Tessa still owe Greg?"""
    # Define the initial debt and the amounts paid and borrowed
    initial_debt = 40
    paid_back = initial_debt / 2
    borrowed = 10

    # Calculate the total debt after the payments and borrowings
    total_debt = initial_debt - paid_back + borrowed

    # Display the remaining debt
    result = total_debt
    return result

print(solution())