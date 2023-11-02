Sorry, there is no solution provided for the Samantha's last name question. Here is the solution for the Oscar's lollipop question:

def solution():
    """Oscar has 24 lollipops and eats 2 on his way to school. He passes 14 out to his friends. He buys twice as many lollipops on his way home as he gave to his friends. He eats 3 more that night and 2 more in the morning. How many lollipops does Oscar have?"""
    initial_lollipops = 24
    lollipops_eaten_on_way_to_school = 2
    lollipops_given_to_friends = 14
    lollipops_bought_on_way_home = lollipops_given_to_friends * 2
    lollipops_eaten_at_night = 3
    lollipops_eaten_in_morning = 2
    
    total_lollipops = initial_lollipops - lollipops_eaten_on_way_to_school + lollipops_bought_on_way_home - lollipops_eaten_at_night - lollipops_eaten_in_morning
    
    result = total_lollipops
    return result

print(solution())