def solution():
    """Michael has a chicken farm. His chickens increase in number by 150 chickens annually. If the number of chickens on his farm now is 550, how many will he have after 9 years?"""
    # Define the number of chickens Michael has now and the annual growth rate
    INITIAL_CHICKENS = 550
    ANNUAL_GROWTH = 150

    # Calculate the number of chickens after 9 years
    num_years = 9
    num_chickens = INITIAL_CHICKENS + (ANNUAL_GROWTH * num_years)

    # Display the number of chickens after 9 years
    result = num_chickens
    return result

print(solution())