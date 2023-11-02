def solution():
    # Calculate Adrianna's total number of pieces of gum
    initial_gum = 10  # initial pieces of gum
    additional_gum = 3  # additional pieces of gum bought
    total_gum = initial_gum + additional_gum  # total pieces of gum
    friends = 11  # number of friends who received gum
    remaining_gum = total_gum - friends  # remaining pieces of gum

    result = remaining_gum
    return result

print(solution())