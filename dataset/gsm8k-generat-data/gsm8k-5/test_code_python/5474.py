def solution():
    # Jan can handle 20 claims
    jan_claims = 20
    # John can handle 30% more claims than Jan
    john_claims = jan_claims * 1.3
    # Missy can handle 15 more claims than John
    missy_claims = john_claims + 15
    result = missy_claims
    return result

print(solution())