def solution():
    principle_amount = 200
    interest_rate = 0.1
    compounds_per_year = 12

    # Calculate the interest added after one month
    monthly_interest_rate = interest_rate / compounds_per_year
    new_principle = principle_amount * (1 + monthly_interest_rate)
    interest_amount = new_principle - principle_amount
    result = interest_amount
    return result

print(solution())