def solution():
    # Calculate the total amount Danielle will pay through the mortgage
    total_amount = 280 - 40  # Danielle paid a $40k deposit, so the total amount she owes through the mortgage is $280k - $40k = $240k
    total_months = 10 * 12  # 10 years is equivalent to 120 months
    monthly_payment = total_amount / total_months  # divide total amount by total months

    # Convert monthly payment to thousands of dollars
    result = monthly_payment / 1000
    return result

print(solution())