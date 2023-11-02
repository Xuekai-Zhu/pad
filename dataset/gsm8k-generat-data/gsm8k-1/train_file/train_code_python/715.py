def solution():
    """Lance has 70 cents, Margaret has three-fourths of a dollar,
    Guy has two quarters and a dime, and Bill has six dimes.
    How many cents do they have combined?"""
    
    lance_cents = 70
    margaret_dollars = 0.75
    guy_cents = 60  # Two quarters and a dime is 60 cents
    bill_cents = 60  # Six dimes is 60 cents
    
    total_cents = lance_cents + (margaret_dollars * 100) + guy_cents + bill_cents
    result = total_cents
    
    return result

print(solution())