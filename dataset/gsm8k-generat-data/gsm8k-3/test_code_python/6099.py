def solution():
    """Rene has three times as many dolls as her sister, while her sister has two more dolls than their grandmother. If their grandmother has 50 dolls, how many dolls do they have altogether?"""
    # Define the number of dolls the grandmother has
    grandmother_dolls = 50

    # Calculate the number of dolls the sister has
    sister_dolls = grandmother_dolls + 2

    # Calculate the number of dolls Rene has
    rene_dolls = sister_dolls * 3

    # Calculate the total number of dolls
    total_dolls = grandmother_dolls + sister_dolls + rene_dolls

    # Display the total number of dolls
    result = total_dolls
    return result

print(solution())