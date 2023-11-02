def solution():
    """On Saturday morning, Renata had $10 to spend. She first went and made a $4 donation in exchange for a ticket to the local charity draw.
    When the draw was done, she was declared the winner of the 5th prize of $90.
    She lost $50 at the first slot machine, $10 at the second and $5 at the last one.
    She picked a $1 bottle of water and while paying for it, she bought a $1 lottery ticket. To her utter delight, she won an instant prize of $65.
    How much money did Renata end up having?"""
    
    # Initial amount Renata has is $10.
    total_amount = 10
    
    # After donating $4, she has $6.
    total_amount -= 4
    
    # Winning the 5th prize adds $90 to her total.
    total_amount += 90
    
    # Losing $50, $10, and $5 while playing slots subtracts $65 from her total.
    total_amount -= 50
    total_amount -= 10
    total_amount -= 5
    
    # Buying a bottle of water and a lottery ticket subtracts $2 from her total.
    total_amount -= 2
    
    # Winning an instant prize of $65 adds $65 to her total.
    total_amount += 65
    
    # Final amount Renata has.
    result = total_amount
    
    return result

print(solution())