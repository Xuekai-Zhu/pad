def solution():
    """Wade has called into a rest stop and decides to get food for the road. He buys a sandwich to eat now, one for the road, and one for in the evening. He also buys 2 drinks. If the drinks cost $4 each and Wade spends a total of $26 then how much, in dollars, did the sandwiches each cost?"""
    num_sandwiches = 3
    num_drinks = 2
    total_spent = 26
    drink_cost = 4
    sandwich_cost = (total_spent - (num_drinks * drink_cost)) / num_sandwiches
    result = sandwich_cost
    return result

print(solution())