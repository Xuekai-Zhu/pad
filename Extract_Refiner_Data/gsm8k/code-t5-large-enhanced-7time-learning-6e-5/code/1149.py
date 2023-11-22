def solution():
    
    # Define the number of seashells collected by Jim
    jim_seashells = 27

    # Calculate the number of seashells collected by Carlos
    carlos_seashells = jim_seashells - 5

    # Calculate the number of seashells collected by Jim
    jim_total_seashells = jim_seashells + carlos_seashells

    # Calculate the total number of seashells collected
    total_seashells = jim_total_seashells + carlos_seashells

    # Calculate the number of seashells each person gets
    each_person_gets = total_seashells / 3

    # Display the number of seashells each person gets
    result = each_person_gets
    return result

print(solution())