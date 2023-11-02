def solution():
    """Sandra's neighbor gives her a basket of 9 eggs every time she babysits their daughter. To make a Spanish flan, she needs 3 eggs. If Sandra has been tasked to make 15 Spanish flans for her school fundraiser, how many times does Sandra have to babysit?"""
    eggs_per_basket = 9
    eggs_per_flan = 3
    flans_to_make = 15
    eggs_needed = flans_to_make * eggs_per_flan
    babysitting_sessions = eggs_needed / eggs_per_basket
    result = babysitting_sessions
    return result

print(solution())