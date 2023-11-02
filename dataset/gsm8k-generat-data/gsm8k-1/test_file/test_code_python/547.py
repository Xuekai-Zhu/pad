def solution():
    """Carly wants to treat her friends. She orders five hamburgers at $4 each, ten packs of potato fries at $0.30 each pack, and five cans of fruit drinks at $2 each can. How much change does Carly get back if she gives one fifty-dollar bill?"""
    
    hamburger_cost = 4
    num_hamburgers = 5
    fries_cost = 0.30
    num_fries = 10
    drink_cost = 2
    num_drinks = 5
    
    total_cost = (hamburger_cost * num_hamburgers) + (fries_cost * num_fries) + (drink_cost * num_drinks)
    change = 50 - total_cost
    
    return change

print(solution())