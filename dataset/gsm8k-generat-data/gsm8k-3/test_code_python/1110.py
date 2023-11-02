def solution():
    """A doctor needs to give medicine to a child, and he knows that he cannot give the same amount of medicine that he would give to an adult. The instructions say that for every kilogram of weight the child must be given 5 ml of medicine. The doctor knows that the child weighs 30 kilograms and that also the full dose has to be given in 3 equal parts. How many milligrams will each part of the dose be?"""
    # Define the amount of medicine per kilogram of weight
    MEDICINE_PER_KG = 5  # ml

    # Define the weight of the child in kilograms
    weight = 30  # kg

    # Calculate the full dose of the medicine for the child
    full_dose = weight * MEDICINE_PER_KG  # ml

    # Calculate the dose for each of the 3 parts
    dose_per_part = full_dose / 3  # ml

    # Display the dose per part in milligrams
    result = dose_per_part * 1000
    return result

print(solution())