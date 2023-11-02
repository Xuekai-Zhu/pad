def solution():
    """Mary has 400 sheep on her farm. She gave a quarter of her sheep to her sister, and half of the remaining sheep to her brother. How many sheep remain with Mary?"""
    # Define the number of sheep Mary has
    total_sheep = 400

    # Calculate the number of sheep given to her sister
    sheep_to_sister = total_sheep // 4

    # Calculate the number of sheep remaining with Mary
    sheep_remaining = total_sheep - sheep_to_sister

    # Calculate the number of sheep given to her brother
    sheep_to_brother = sheep_remaining // 2

    # Calculate the final number of sheep remaining with Mary
    sheep_final = sheep_remaining - sheep_to_brother

    # Display the final number of sheep remaining with Mary
    result = sheep_final
    return result

print(solution())