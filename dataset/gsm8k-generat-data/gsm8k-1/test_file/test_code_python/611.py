def solution():
    """Scarlett found an aquarium for $10.00 at a yard sale. At the pet store, she bought 2 bags of rocks for $2.50 each and 3 pieces of coral at $2.00 apiece. She bought 20 fish at $0.50 each and she needed fish food that cost $2.00. How much did she spend?"""
    aquarium_cost = 10
    rock_bags = 2
    rock_cost = 2.5
    coral_pieces = 3
    coral_cost = 2
    fish_amount = 20
    fish_cost = 0.5
    fish_food_cost = 2
    
    total_cost = aquarium_cost + (rock_bags * rock_cost) + (coral_pieces * coral_cost) + (fish_amount * fish_cost) + fish_food_cost
    result = total_cost
    return result

print(solution())