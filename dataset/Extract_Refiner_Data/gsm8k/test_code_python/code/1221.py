def solution():
    
    # Define the number of people and treats per person
    num_people = 5
    treats_per_person = 2

    # Calculate the total number of treats
    total_treats = num_people * treats_per_person

    # Calculate the number of cupcakes
    num_cupcakes = (total_treats + 2) / 3

    # Display the number of cupcakes
    result = num_cupcakes
    return result

print(solution())