def solution():
    """Chris is trying to sell his car for $5200 and has gotten two price offers. One buyer offered to pay the full price
    if Chris would pay for the car maintenance inspection, which cost a tenth of Chris’s asking price. The other buyer agreed
    to pay the price if Chris replaced the headlights for $80 and the tires for three times as much. What is the difference 
    between the amounts Chris will earn from the two offers?"""
    
    # Define the asking price of the car
    price = 5200
    
    # Calculate the cost of the maintenance inspection
    inspection_cost = price / 10
    
    # Calculate the cost of replacing the headlights and tires
    headlight_cost = 80
    tire_cost = 3 * headlight_cost
    
    # Calculate the earnings from the first offer
    earnings1 = price - inspection_cost
    
    # Calculate the earnings from the second offer
    earnings2 = price - headlight_cost - tire_cost
    
    # Calculate the difference between the two earnings
    difference = earnings1 - earnings2
    
    # Display the difference in earnings
    result = difference
    return result

print(solution())