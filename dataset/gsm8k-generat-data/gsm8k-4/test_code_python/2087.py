def solution():
    """A private company raised $2500 to be used for charity. They donated 80% to a public foundation with 8 organizations. How much money will each organization receive?"""
    # Define the total amount raised and the percentage donated
    total_amount = 2500
    donation_percentage = 0.8

    # Calculate the amount donated to the public foundation
    donated_amount = total_amount * donation_percentage

    # Calculate the amount donated to each organization
    organization_amount = donated_amount / 8

    # Return the result
    result = organization_amount
    return result

print(solution())