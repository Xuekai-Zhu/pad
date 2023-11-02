def solution():
    """The P.T.O. decided to provide shirts for the elementary students for track and field day. Each grade was given a different color. 101 Kindergartners wore orange shirts that cost $5.80 each. 113 first graders wore yellow shirts that cost $5 each. 107 second graders wore blue shirts that cost $5.60 each. 108 third graders wore green shirts that cost $5.25 each. How much did the P.T.O. spend on shirts for field day?"""
    k_shirts = 101
    k_price = 5.80
    f_shirts = 113
    f_price = 5.00
    s_shirts = 107
    s_price = 5.60
    t_shirts = 108
    t_price = 5.25
    
    total_spent = (k_shirts * k_price) + (f_shirts * f_price) + (s_shirts * s_price) + (t_shirts * t_price)
    result = total_spent
    return result

print(solution())