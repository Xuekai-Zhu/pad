def solution():
    """Mary is paying her monthly garbage bill for a month with exactly four weeks. The garbage company charges Mary $10 per trash bin and $5 per recycling bin every week, and Mary has 2 trash bins and 1 recycling bin. They're giving her an 18% discount on the whole bill before fines for being elderly, but also charging her a $20 fine for putting inappropriate items in a recycling bin. How much is Mary's garbage bill?"""
    trash_bins = 2
    recycling_bins = 1
    trash_price = 10
    recycling_price = 5
    weeks = 4
    discount = 0.18
    fine = 20

    total_cost = ((trash_price * trash_bins + recycling_price * recycling_bins) * weeks) - fine
    discounted_cost = total_cost * (1 - discount)

    result = discounted_cost
    return result

print(solution())