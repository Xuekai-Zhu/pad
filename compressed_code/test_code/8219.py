def solution():
    
    cups_veggies_per_serving = 1
    cups_broth_per_serving = 2.5
    total_cups_veggies = cups_veggies_per_serving * 8
    total_cups_broth = cups_broth_per_serving * 8
    total_pints = (total_cups_veggies + total_cups_broth) / 2
    result = total_pints
    return result

print(solution())