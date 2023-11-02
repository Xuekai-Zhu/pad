def solution():
    """Half of Taylor's house guests like weak coffee and the other half like strong coffee in the morning.  Taylor uses 1 tablespoon of coffee per cup of water to make it weak and he doubles that amount to make it strong.  
    If he makes 12 cups of both weak and strong coffee, how many tablespoons of coffee will he need?"""
    
    # Define the number of cups for each type of coffee
    cups_weak = 12
    cups_strong = 12

    # Calculate the total number of tablespoons of coffee needed for weak and strong coffee
    coffee_weak = cups_weak * 1
    coffee_strong = cups_strong * 2

    # Calculate the total number of tablespoons of coffee needed
    total_coffee = coffee_weak + coffee_strong

    result = total_coffee
    return result

print(solution())