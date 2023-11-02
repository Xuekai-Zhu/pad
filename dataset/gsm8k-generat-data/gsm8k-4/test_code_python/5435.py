def solution():
    """Matt's protein powder is 80% protein. He weighs 80 kg and wants to eat 2 grams of protein per kilogram of body weight each day. How much protein powder does he need to eat per week?"""
    # Define Matt's weight and protein intake
    weight = 80
    protein_intake = weight * 2 * 7

    # Define the protein content of the powder
    protein_content = 0.8

    # Calculate the total amount of powder needed to meet his protein intake
    powder_needed = protein_intake / protein_content

    # return the result in grams
    result = powder_needed * 1000
    return result

print(solution())