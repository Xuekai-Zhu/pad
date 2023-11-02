def solution():
    """Dorchester works at a puppy wash. He is paid $40 per day + $2.25 for each puppy he washes. On Wednesday, Dorchester earned $76. How many puppies did he wash that day?"""
    # Define Dorchester's daily pay and the amount he earns per puppy
    DAILY_PAY = 40
    PER_PUPPY_PAY = 2.25

    # Define the total amount Dorchester earned on Wednesday
    total_earnings = 76

    # Subtract the daily pay from the total earnings to find the amount earned from washing puppies
    puppy_earnings = total_earnings - DAILY_PAY

    # Divide the puppy earnings by the amount earned per puppy to find the number of puppies washed
    puppies_washed = int(puppy_earnings / PER_PUPPY_PAY)

    # return the result
    result = puppies_washed
    return result

print(solution())