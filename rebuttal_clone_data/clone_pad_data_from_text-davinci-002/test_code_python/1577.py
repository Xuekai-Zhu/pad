def solution():
    starting_amount = 100
    interest_rate = 10
    num_years = 2
    amount = starting_amount
    for i in range(0, num_years):
        interest = amount * (interest_rate / 100)
        amount = interest + amount
    result = amount
    return result

print(solution())