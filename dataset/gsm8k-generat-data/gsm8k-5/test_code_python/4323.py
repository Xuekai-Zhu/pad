def solution():
    number_of_puppies = 7  # Sandra's dog gave birth to 7 puppies
    portions_of_formula = 105  # Sandra has 105 portions of formula
    days = 5  # Sandra needs to give the formula to the puppies for 5 days

    # Calculate the total number of portions needed for all the puppies for 5 days
    total_portions_needed = number_of_puppies * days

    # Calculate the number of times Sandra should feed the puppies per day
    times_to_feed = total_portions_needed / portions_of_formula
    result = times_to_feed
    return result

print(solution())