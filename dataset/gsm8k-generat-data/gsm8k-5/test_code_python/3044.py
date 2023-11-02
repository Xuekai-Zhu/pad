def solution():
    beef = 10  # Tom has 10 pounds of beef
    noodles_per_beef = 2  # It takes 2 times more noodles than beef to make lasagna
    noodles_needed = beef * noodles_per_beef  # Calculate the amount of noodles needed
    noodles_already_have = 4  # Tom already has 4 pounds of noodles
    noodles_to_buy = noodles_needed - noodles_already_have  # Calculate the amount of noodles to buy
    noodles_per_package = 2  # Noodles come in 2-pound packages
    packages_to_buy = noodles_to_buy / noodles_per_package  # Calculate the number of packages to buy
    result = packages_to_buy
    return result

print(solution())