def solution():
    
    # Define the number of seashells found by each person
    tom_seashells = 214
    nancy_seashells = 432
    benny_seashells = 86

    # Calculate the total number of seashells found
    total_seashells = tom_seashells + nancy_seashells + benny_seashells

    # Subtract the number of cracked seashells
    good_seashells = total_seashells - 67

    # Display the number of good seashells found
    result = good_seashells
    return result

print(solution())