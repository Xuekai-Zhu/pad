def solution():
    
    jan_claims = 20
    john_claims = jan_claims * 1.3
    missy_claims = john_claims + 15
    total_claims = jan_claims + john_claims + missy_claims
    result = missy_claims
    return result

print(solution())