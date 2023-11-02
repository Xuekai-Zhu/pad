def solution():
    carlo_age = 40  # given that Carlo Rosi is 40 years old
    twin_age = carlo_age / 4  # given that Carlo Rosi is four times older than Twin Valley
    franzia_age = carlo_age * 3  # given that Franzia is three times as old as Carlo Rosi

    # Calculate the total age of the three brands of wine
    total_age = carlo_age + twin_age + franzia_age
    result = total_age
    return result

print(solution())