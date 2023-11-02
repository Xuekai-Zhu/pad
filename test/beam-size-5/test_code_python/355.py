def solution():
    
    # Define the initial amount of money Billy has
    initial_money = 10

    # Calculate the amount of money Billy spent on gumballs
    gumball_cost = 40 * 0.05

    # Calculate the amount of money Billy spent on candy
    candy_cost = (initial_money - gumball_cost) / 1.5

    # Calculate the pounds of candy Billy bought
    pounds_of_candy = candy_cost / 1.5

    # Display the pounds of candy Billy bought
    result = pounds_of_candy
    return result

print(solution())