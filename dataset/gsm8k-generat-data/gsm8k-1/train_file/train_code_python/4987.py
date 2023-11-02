def solution():
    """Greg has lent his sister Tessa money on several occasions. Greg writes down all of his sister's debts in a notebook, the first time he lent her $40. A week later, Tessa paid him back half of her debt. A few days later she asked him for $10 more. How much does Tessa still owe Greg?"""
    initial_debt = 40
    half_debt = initial_debt / 2
    new_debt = half_debt + 10
    amount_paid = half_debt
    amount_owed = initial_debt - amount_paid + new_debt
    result = amount_owed
    return result

print(solution())