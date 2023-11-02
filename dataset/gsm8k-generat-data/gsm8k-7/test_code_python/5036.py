def solution():
    starting_lollipops = 42
    emily_lollipops = starting_lollipops * (2/3) # 2/3 of starting lollipops
    remaining_lollipops = starting_lollipops - emily_lollipops # Marlon keeps the remaining lollipops
    remaining_lollipops -= 4 # Marlon keeps 4 more lollipops
    lou_lollipops = remaining_lollipops # All remaining lollipops go to Lou
    result = lou_lollipops
    return result

print(solution())