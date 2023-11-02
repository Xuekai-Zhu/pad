def solution():
    """A doctor needs to give medicine to a child, and he knows that he cannot give the same amount of medicine that he would give to an adult. The instructions say that for every kilogram of weight the child must be given 5 ml of medicine. The doctor knows that the child weighs 30 kilograms and that also the full dose has to be given in 3 equal parts. How many milligrams will each part of the dose be?"""
    # Define the weight of the child and the dosage per kilogram
    child_weight = 30
    dosage_per_kg = 5

    # Calculate the total dosage needed for the child
    total_dosage = child_weight * dosage_per_kg

    # Divide the total dosage into 3 equal parts
    part_dosage = total_dosage / 3

    result = part_dosage
    return result

print(solution())