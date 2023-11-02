def solution():
    # Define the weight loss of the first person
    person1_loss = 27

    # Define the weight loss of the second person
    person2_loss = person1_loss - 7

    # Calculate the total weight loss of the last two people
    last2_total_loss = 103 - person1_loss - person2_loss

    # Divide the total weight loss of the last two people by 2 to find their individual weight loss
    last2_individual_loss = last2_total_loss / 2
    result = last2_individual_loss
    return result

print(solution())