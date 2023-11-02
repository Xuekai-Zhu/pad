def solution():
    # Define what vegans do not eat
    non_vegan_food = ["milk", "eggs", "meat", "cheese"]
    # Check if chickpeas are a vegan alternative for tuna
    tuna_alternative = "chickpeas"
    if tuna_alternative not in non_vegan_food:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())