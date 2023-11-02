def solution():
    # Calculate the number of claims John can handle
    john_claims = 20 * 1.3  # John can handle 30% more claims than Jan

    # Calculate the number of claims Missy can handle
    missy_claims = john_claims + 15  # Missy can handle 15 more claims than John

    result = missy_claims
    return result

print(solution())