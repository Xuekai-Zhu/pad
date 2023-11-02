def solution():
    """Greg has lent his sister Tessa money on several occasions. Greg writes down all of his sister's debts in a notebook, the first time he lent her $40. A week later, Tessa paid him back half of her debt. A few days later she asked him for $10 more. How much does Tessa still owe Greg?"""
    first_lend = 40
    repay_1 = first_lend / 2
    lend_2 = repay_1 + 10
    total_debt = first_lend + lend_2
    repaid = repay_1
    still_owed = total_debt - repaid
    result = still_owed
    return result

print(solution())