def solution():
    """Kathryn moved to a new city for the new job she had landed two weeks ago.
    Her rent was $1200, 1/2 of what she spent on food and travel expenses in a month.
    Luckily, she found a new friend Shelby, who moved in with her to share the rent.
    If her salary was $5000 per month, how much money remained after her expenses?"""
    rent = 1200
    expenses = rent * 2
    salary = 5000
    remaining_money = salary - (expenses / 2)
    result = remaining_money
    return result

print(solution())