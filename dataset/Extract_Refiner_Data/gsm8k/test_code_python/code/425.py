def solution():
    
    # Define the number of letters in Indras' name
    indras_letters = 6

    # Calculate the number of letters in the sister's name
    sister_letters = (indras_letters / 2) + 4

    # Calculate the total number of letters in both names
    total_letters = indras_letters + sister_letters

    # Display the total number of letters
    result = total_letters
    return result

print(solution())