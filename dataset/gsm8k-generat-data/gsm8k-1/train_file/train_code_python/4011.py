def solution():
    """Michael has 2 cats and 3 dogs. He needs to pay a friend to watch them, who charges $13 a night per animal. How much does Michael have to pay?"""
    cats = 2
    dogs = 3
    cost_per_night = 13
    total_nights = 7 # assuming Michael is going away for a week
    total_animals = cats + dogs
    total_cost = total_animals * cost_per_night * total_nights
    result = total_cost
    return result

print(solution())