def solution():
    current_chickens = 550  # Michael has 550 chickens currently
    annual_increase = 150  # Michael's chickens increase in number by 150 annually
    years = 9  # Michael wants to know how many chickens he will have after 9 years

    # Calculate the total number of chickens Michael will have after 9 years
    total_chickens = current_chickens + (annual_increase * years)
    result = total_chickens
    return result

print(solution())