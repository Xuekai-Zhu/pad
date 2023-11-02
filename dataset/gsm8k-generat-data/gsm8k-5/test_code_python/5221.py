def solution():
    eggs_available = 60  # The chef has 60 eggs
    eggs_in_fridge = 10  # The chef puts 10 eggs in the fridge
    eggs_for_cakes = eggs_available - eggs_in_fridge  # The rest of the eggs are used to make cakes
    eggs_per_cake = 5  # The chef uses 5 eggs to make one cake

    # Calculate the number of cakes the chef makes
    num_cakes = eggs_for_cakes // eggs_per_cake
    result = num_cakes
    return result

print(solution())