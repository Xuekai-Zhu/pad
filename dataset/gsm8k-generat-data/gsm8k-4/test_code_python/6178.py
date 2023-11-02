def solution():
    """Ibrahim wants to buy an MP3 player for 120 euros and a CD for 19 euros. He has 55 euros in savings. His father participates in his purchase by giving him 20 euros. How much money does Ibrahim lack?"""
    # Define the prices of the MP3 player and the CD
    mp3_price = 120
    cd_price = 19
    
    # Define the amount of money Ibrahim has
    savings = 55
    
    # Define the amount of money Ibrahim's father gives him
    father_contribution = 20
    
    # Calculate the total amount that Ibrahim can spend
    total_budget = savings + father_contribution
    
    # Calculate the total cost of the MP3 player and the CD
    total_cost = mp3_price + cd_price
    
    # Calculate the amount of money Ibrahim lacks
    money_lack = total_cost - total_budget
    
    # return the result
    result = money_lack
    return result

print(solution())