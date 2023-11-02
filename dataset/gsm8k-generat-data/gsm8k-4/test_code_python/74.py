def solution():
    """Four people lost a total of 103 kilograms of weight. The first person lost 27 kilograms. The second person lost 7 kilograms less than the first person. The two remaining people lost the same amount. How many kilograms did each of the last two people lose?"""
    # Define the weight loss of the first person
    person1_loss = 27

    # Calculate the weight loss of the second person
    person2_loss = person1_loss - 7

    # Calculate the total weight loss of the first two people
    first_two_loss = person1_loss + person2_loss

    # Calculate the total weight loss of the last two people
    last_two_loss = 103 - first_two_loss

    # Divide the weight loss of the last two people equally
    each_loss = last_two_loss / 2

    # Return the weight loss of each of the last two people
    result = each_loss
    return result

print(solution())