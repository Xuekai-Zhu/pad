def solution():
    """Victory and Sam have saved money for their holiday spending. Victory saves $100 less than Sam. If Sam saves $1000, how much is the total money saved for holiday spending?"""
    # Define Sam's savings
    sam_savings = 1000

    # Calculate Victory's savings
    victory_savings = sam_savings - 100

    # Calculate the total savings of both Victory and Sam
    total_savings = victory_savings + sam_savings

    # return the result
    result = total_savings
    return result

print(solution())