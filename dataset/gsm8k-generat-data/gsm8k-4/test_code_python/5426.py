def solution():
    """Michael has a chicken farm. His chickens increase in number by 150 chickens annually. If the number of chickens on his farm now is 550, how many will he have after 9 years?"""
    # Define the initial number of chickens and the annual increase
    initial_chickens = 550
    annual_increase = 150

    # Calculate the number of chickens after 9 years
    chicken_count = initial_chickens + (annual_increase * 9)

    # Return the result
    result = chicken_count
    return result

print(solution())