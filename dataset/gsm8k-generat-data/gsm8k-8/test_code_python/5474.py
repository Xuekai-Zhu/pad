def solution():
    # Define the number of claims Jan can handle
    jan_claims = 20

    # Calculate the number of claims John can handle
    john_claims = jan_claims * 1.3

    # Calculate the number of claims Missy can handle
    missy_claims = john_claims + 15

    result = int(missy_claims)
    return result

print(solution())