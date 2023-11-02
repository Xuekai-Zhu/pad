def solution():
    """James decides he needs to start eating more vegetables. He starts by eating a quarter pound of asparagus and a quarter pound of broccoli per day. After 2 weeks, he doubles that amount and adds 3 pounds of kale per week. How many pounds of vegetables does he eat a week after adding the kale?"""
    
    # Calculate the initial amount of asparagus and broccoli James eats in one week
    initial_veggies = (0.25 * 7 * 2) + (0.25 * 7 * 2)  # quarter pound each day, for 2 weeks and doubled
    # Add the amount of kale he eats in one week after adding it
    total_veggies = initial_veggies + (3 * 2)  # 3 pounds per week, for 2 weeks
    # Return the result
    result = total_veggies
    return result

print(solution())