def solution():
    """Tyson decided to make muffaletta sandwiches for the big game. Each sandwich required 1 pound each of meat and cheese and would serve 4 people. There would be 20 people in total watching the game. The meat cost $7.00 per pound and the cheese cost $3.00 per pound. How much money would he spend on the meat and cheese to make enough sandwiches to serve 20 people?"""
    people = 20
    sandwiches = people / 4
    meat_per_sandwich = 1
    cheese_per_sandwich = 1
    meat_cost_per_pound = 7
    cheese_cost_per_pound = 3
    meat_cost = sandwiches * meat_per_sandwich * meat_cost_per_pound
    cheese_cost = sandwiches * cheese_per_sandwich * cheese_cost_per_pound
    total_cost = meat_cost + cheese_cost
    result = total_cost
    return result

print(solution())