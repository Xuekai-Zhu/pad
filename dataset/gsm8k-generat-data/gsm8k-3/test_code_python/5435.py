def solution():
    """Matt's protein powder is 80% protein.  He weighs 80 kg and wants to eat 2 grams of protein per kilogram of body weight each day.  How much protein powder does he need to eat per week?"""
    # Define Matt's weight and protein intake
    weight = 80
    protein_intake = 2 # in grams of protein per kilogram of body weight

    # Calculate Matt's daily protein requirement in grams
    daily_protein_requirement = weight * protein_intake

    # Calculate the daily amount of protein powder Matt needs to eat
    daily_protein_powder = daily_protein_requirement / 0.8 # protein powder is 80% protein

    # Calculate the weekly amount of protein powder Matt needs to eat
    weekly_protein_powder = daily_protein_powder * 7

    # Display the weekly amount of protein powder Matt needs to eat
    result = weekly_protein_powder
    return result

print(solution())