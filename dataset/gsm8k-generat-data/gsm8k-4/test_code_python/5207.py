def solution():
    """Geric had twice as many bills as Kyla who has 2 fewer bills than Jessa. After giving 3 bills to Geric, Jessa has 7 bills left. How many bills did Geric have at the beginning?"""
    
    # Let's assume that Kyla has 'k' bills, then Jessa has 'k+2' bills, and Geric has '2k' bills
    # After giving 3 bills, Jessa has 'k+2-3=k-1' bills left
    # And we know that Jessa has 7 bills left, so we can solve for 'k'
    
    k = 8  # Jessa has 10 bills initially (k+2), and after giving 3 bills she has 7 left
    
    # Now that we know 'k', we can solve for the number of bills Geric had at the beginning (2k)
    geric_bills = 2 * k
    
    result = geric_bills
    return result

print(solution())