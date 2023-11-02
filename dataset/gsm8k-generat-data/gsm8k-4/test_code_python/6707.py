def solution():
    """Mary has 400 sheep on her farm. She gave a quarter of her sheep to her sister, and half of the remaining sheep to her brother. How many sheep remain with Mary?"""
    # Define the initial number of sheep
    initial_sheep = 400

    # Calculate the number of sheep given to Mary's sister
    sister_sheep = initial_sheep // 4

    # Calculate the number of remaining sheep
    remaining_sheep = initial_sheep - sister_sheep

    # Calculate the number of sheep given to Mary's brother
    brother_sheep = remaining_sheep // 2

    # Calculate the number of sheep remaining with Mary
    mary_sheep = remaining_sheep - brother_sheep

    # Return the result
    result = mary_sheep
    return result

print(solution())