def solution():
    """The chef has 60 eggs. He puts 10 eggs in the fridge and uses the rest to make cakes. If he used 5 eggs to make one cake, how many cakes did the chef make?"""
    total_eggs = 60
    eggs_in_fridge = 10
    eggs_for_cakes = total_eggs - eggs_in_fridge
    eggs_per_cake = 5
    cakes = eggs_for_cakes // eggs_per_cake
    result = cakes
    return result

print(solution())