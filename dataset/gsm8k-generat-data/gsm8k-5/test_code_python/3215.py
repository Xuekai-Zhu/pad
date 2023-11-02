def solution():
    original_volume = 500  # The original volume of the balloon is 500cm³
    growth_factor = 2/5  # The balloon increases by two-fifths of its previous volume every hour
    time = 2  # The balloon is underwater for 2 hours

    # Calculate the final volume of the balloon
    final_volume = original_volume * (1 + growth_factor) ** time
    result = final_volume
    return result

print(solution())