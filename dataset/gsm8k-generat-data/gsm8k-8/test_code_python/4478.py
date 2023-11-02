def solution():
    # Define Lulu's savings
    lulu_savings = 6

    # Calculate Nora's and Tamara's savings
    nora_savings = 5 * lulu_savings
    tamara_savings = nora_savings / 3

    # Calculate the total amount saved
    total_savings = lulu_savings + nora_savings + tamara_savings

    # Calculate the remaining amount after paying off the debt
    remaining_amount = total_savings - 40

    # Calculate how much each girl will get
    amount_per_girl = remaining_amount / 3
    result = amount_per_girl
    return result

print(solution())