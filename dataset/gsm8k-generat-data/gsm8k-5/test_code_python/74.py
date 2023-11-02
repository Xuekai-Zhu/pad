def solution():
    # Total weight lost by all four people
    total_weight_lost = 103

    # Person 1's weight loss
    person1_weight_loss = 27

    # Person 2's weight loss is 7 less than person 1's weight loss
    person2_weight_loss = person1_weight_loss - 7

    # Sum of weight loss by person 3 and person 4
    sum_weight_loss_p3_p4 = total_weight_lost - person1_weight_loss - person2_weight_loss

    # As person 3 and person 4 have lost the same amount of weight, divide their total weight loss by 2
    weight_loss_per_person_p3_p4 = sum_weight_loss_p3_p4 / 2

    result = weight_loss_per_person_p3_p4
    return result

print(solution())