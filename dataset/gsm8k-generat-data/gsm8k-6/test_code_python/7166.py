def solution():
    # Find the number of degrees Jolly has
    degrees_Jolly = (150 - 5) / 2  # Summer has 5 more degrees than Jolly, so Jolly has 5 less degrees than Summer. Divide the remaining degrees equally between them.
    
    # Calculate the combined number of degrees they both have
    total_degrees = degrees_Jolly + 150
    result = total_degrees
    return result

print(solution())