def solution():
    """Carla is dividing up insurance claims among 3 agents. Missy can handle 15 more claims than John, who can handle 30% more claims than Jan. If Jan can handle 20 claims, how many claims can Missy handle?"""
    # Define the number of claims Jan can handle
    jan_claims = 20

    # Calculate the number of claims John can handle (30% more than Jan)
    john_claims = jan_claims * 1.3

    # Calculate the number of claims Missy can handle (15 more than John)
    missy_claims = john_claims + 15

    # Display the number of claims Missy can handle
    result = missy_claims
    return result

print(solution())