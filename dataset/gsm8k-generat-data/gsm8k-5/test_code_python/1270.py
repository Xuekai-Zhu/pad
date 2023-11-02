def solution():
    house_price = 280  # The house costs $280k
    deposit = 40  # Danielle pays a $40k deposit
    mortgage = house_price - deposit  # Danielle finances the rest with a mortgage
    years = 10  # The mortgage is spread out over 10 years
    months = years * 12  # The mortgage is paid in monthly installments

    # Calculate the monthly payment needed to pay off the mortgage in 10 years
    monthly_payment = mortgage / months
    result = monthly_payment
    return result

print(solution())