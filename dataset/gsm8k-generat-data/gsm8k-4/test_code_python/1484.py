def solution():
    """Lucy lost one-third of her money. She then spent one-fourth of the remainder, and only left with $15. How much money did Lucy have at the beginning?"""
    # Let X be the amount of money Lucy had at the beginning
    # After losing one-third, she has 2/3*X remaining
    remaining_one = 2/3*X
    
    # After spending one-fourth of the remainder, she has 3/4*(2/3*X) = 1/2*X remaining
    remaining_two = 1/2*X
    
    # If she is left with $15, then she spent X - $15
    spent_money = X - 15
    
    # Combining the above equations, we have the equation:
    # X - (1/2*X + 15) = spent_money
    # Solving for X,
    # X = spent_money * (-2)
    
    X = spent_money * (-2)
    
    result = X
    return result

print(solution())