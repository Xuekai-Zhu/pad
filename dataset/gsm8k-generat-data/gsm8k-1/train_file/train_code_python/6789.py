def solution():
    """Quentin, Skylar, and Colten have a total of 383 chickens. Quentin has 25 more than double the chickens that Skylar has. Skylar has 4 less than triple the number of chickens that Colten has. How many chickens does Colten have?"""
    total_chickens = 383
    q_s_ratio = 2 # Quentin has double the number of chickens as Skylar
    s_c_ratio = 3 # Skylar has 3 times the number of chickens as Colten
    q_s_diff = 25 # Quentin has 25 more chickens than double the number Skylar has
    s_c_diff = 4 # Skylar has 4 less chickens than triple the number Colten has
    
    # Let's create the system of equations:
    # Q + S + C = 383
    # Q = 2S + 25
    # S = 3C - 4
    
    # Replace Q in terms of S and C in the equation Q + S + C = 383
    # 2S + 25 + S + C = 383
    # 3S + C = 358
    
    # Replace S in terms of C and solve for C
    # 3(3C-4) + C = 358
    # 10C = 370
    # C = 37
    
    colten_chickens = 37
    result = colten_chickens
    return result

print(solution())