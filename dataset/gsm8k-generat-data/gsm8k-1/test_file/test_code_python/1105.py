def solution():
    """Three of the women at the cocktail party are wearing 4 inch heels and three are wearing 2 inch heels. What is the average height of heels at this party?"""
    num_4in = 3
    num_2in = 3
    height_4in = 4
    height_2in = 2
    total_height = (num_4in * height_4in) + (num_2in * height_2in)
    num_women = num_4in + num_2in
    avg_height = total_height / num_women
    result = avg_height
    
    return result

print(solution())