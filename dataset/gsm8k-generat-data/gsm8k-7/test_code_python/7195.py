def solution():
    daily_pay = 40
    per_puppy_pay = 2.25
    wed_earnings = 76

    # Calculate the amount earned from washing puppies
    puppy_earnings = wed_earnings - daily_pay

    # Calculate the number of puppies washed
    num_puppies = puppy_earnings / per_puppy_pay
    result = num_puppies
    return result

print(solution())