def solution():
    # Calculate the total cost for each person
    sonja_cost = 3 + 23  # Sonja buys a loaf of bread and a platter of cold cuts
    barbara_cost = 1*5 + 2*2  # Barbara buys soda for 5 people and 2 boxes of crackers
    mario_rick_cost = 2*3/2  # Mario and Rick split the cost of 2 packages of Cheese Doodles
    danica_cost = 4  # Danica buys a package of paper plates
    total_spent = sonja_cost + barbara_cost + mario_rick_cost + danica_cost  # Calculate the total amount spent by all people
    others_spent = barbara_cost + mario_rick_cost + danica_cost  # Calculate the amount spent by the rest of the office
    difference = sonja_cost - others_spent  # Calculate the difference in cost
    result = difference
    return result

print(solution())