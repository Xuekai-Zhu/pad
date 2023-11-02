def solution():
    """Lisa is making a pizza. She uses 30 pieces of pepperoni for a pizza, twice as many pieces of ham, and 12 more pieces of sausage than pepperoni. If there are 6 slices of pizza, and everything was distributed evenly, how many pieces of meat altogether are on each slice?"""
    # Define the number of pieces of pepperoni
    pepperoni = 30

    # Define the number of pieces of ham
    ham = pepperoni * 2

    # Define the number of pieces of sausage
    sausage = pepperoni + 12

    # Calculate the total number of pieces of meat
    total_meat = pepperoni + ham + sausage

    # Calculate the number of pieces of meat on each slice of pizza
    meat_per_slice = total_meat / 6

    result = meat_per_slice
    return result

print(solution())