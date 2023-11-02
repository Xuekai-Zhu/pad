def solution():
    """James goes to pet smart to adopt a puppy.  The adoption fee is $200 and his friend agrees to pay 25% of that.  How much does James have to pay?"""
    # Define the adoption fee and the friend's contribution percentage
    adoption_fee = 200
    friend_contribution = 0.25

    # Calculate the friend's contribution
    friend_payment = adoption_fee * friend_contribution

    # Calculate James's payment
    james_payment = adoption_fee - friend_payment

    # Display James's payment
    result = james_payment
    return result

print(solution())