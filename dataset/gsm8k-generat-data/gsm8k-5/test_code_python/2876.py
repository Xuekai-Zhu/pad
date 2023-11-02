def solution():
    guitar_cost = 1200  # The guitar costs $1200
    interest_rate = 0.1  # The interest rate is 10%
    total_loan = guitar_cost + (guitar_cost * interest_rate)  # Aaron's father will lend him the guitar cost plus the interest
    total_payments = 12  # Aaron will make 12 payments of $100 each

    # Calculate the total amount owed at the end of the payment plan
    total_owed = total_loan + (total_payments * 100)

    result = total_owed
    return result

print(solution())