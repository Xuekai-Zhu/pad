def solution():
    mandy_bills = 3
    mandy_denomination = 20
    manny_bills = 2
    manny_denomination = 50
    exchange_denomination = 10

    # Calculate the total amount of money Mandy has
    mandy_total = mandy_bills * mandy_denomination

    # Calculate the total amount of money Manny has
    manny_total = manny_bills * manny_denomination

    # Calculate the total amount of money they can exchange
    exchange_total = mandy_total + manny_total

    # Calculate the number of $10 bills they can get
    num_exchange_bills = exchange_total / exchange_denomination

    # Calculate the number of $10 bills Manny will have more than Mandy
    num_extra_bills = (manny_bills * manny_denomination)/exchange_denomination - (mandy_bills * mandy_denomination)/exchange_denomination

    result = num_extra_bills
    return result

print(solution())