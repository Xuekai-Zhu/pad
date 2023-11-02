def solution():
    """James goes to pet smart to adopt a puppy. The adoption fee is $200 and his friend agrees to pay 25% of that. How much does James have to pay?"""
    # Define the adoption fee
    adoption_fee = 200

    # Calculate the amount that the friend will pay
    friend_payment = adoption_fee * 0.25

    # Calculate the amount that James will have to pay
    james_payment = adoption_fee - friend_payment

    # Return the result
    result = james_payment
    return result

print(solution())