def solution():
    """Ricciana and Margarita joined in their school's long jump event. Ricciana ran and jumped a total of 24 feet -  20 feet for running and 4 feet for jumping. Margarita ran for 18 feet and jumped 1 foot less than twice Ricciana's jump. How much farther did Margarita run and jump than Ricciana?"""
    
    # Calculate Ricciana's total jump distance
    ricciana_jump = 4
    
    # Calculate Margarita's jump distance
    margarita_jump = ((2 * ricciana_jump) - 1)
    
    # Calculate Ricciana's total distance
    ricciana_distance = 20 + ricciana_jump
    
    # Calculate Margarita's total distance
    margarita_distance = 18 + margarita_jump
    
    # Calculate the difference in distance between Margarita and Ricciana
    difference = margarita_distance - ricciana_distance
    
    # Display the difference in distance
    result = difference
    return result

print(solution())