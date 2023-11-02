def solution():
    total_weight_loss = 103
    person1_loss = 27
    person2_loss = person1_loss - 7
    remaining_loss = total_weight_loss - person1_loss - person2_loss
    num_remaining_people = 2
    # Divide remaining weight loss equally among the two people
    person3_loss = person4_loss = remaining_loss / num_remaining_people
    result = (person3_loss, person4_loss)
    return result

print(solution())