def solution():
    """Carla is dividing up insurance claims among 3 agents. Missy can handle 15 more claims than John, who can handle 30% more claims than Jan. If Jan can handle 20 claims, how many claims can Missy handle?"""
    jan_claims = 20
    john_claims = jan_claims * 1.3
    missy_claims = john_claims + 15
    total_claims = jan_claims + john_claims + missy_claims
    result = missy_claims
    return result

print(solution())