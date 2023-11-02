def solution():
    num_dogs = 2
    dog_price = 250.0
    num_puppies = 6
    puppy_price = 350.0

    # Calculate the total cost of the two show dogs
    total_dog_cost = num_dogs * dog_price

    # Calculate the total revenue from selling the 6 puppies
    total_puppy_revenue = num_puppies * puppy_price

    # Calculate the profit made from the breeding business
    total_profit = total_puppy_revenue - total_dog_cost
    result = total_profit
    return result

print(solution())