def solution():
    
    cost_per_dog = 250
    number_of_dogs = 2
    total_cost = cost_per_dog * number_of_dogs
    price_per_puppy = 350
    number_of_puppies = 6
    total_income = price_per_puppy * number_of_puppies
    total_profit = total_income - total_cost
    result = total_profit
    return result

print(solution())