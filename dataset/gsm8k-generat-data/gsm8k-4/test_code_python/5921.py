def solution():
    """Freddy is calling his family on New Year's Eve. He calls his dad, who lives in the same city as him, and they talk for 45 minutes. Then he calls his brother, who lives on the other side of the world, and they talk for 31 minutes. Local calls cost 5 cents a minute, while international calls cost 25 cents a minute. How many dollars did Freddy spend calling his family on New Year's Eve?"""
    # Define the call rates
    LOCAL_RATE = 0.05
    INTERNATIONAL_RATE = 0.25

    # Calculate the cost of calling Freddy's dad
    dad_cost = 45 * LOCAL_RATE

    # Calculate the cost of calling Freddy's brother
    brother_cost = 31 * INTERNATIONAL_RATE

    # Calculate the total cost of calling
    total_cost = dad_cost + brother_cost

    # Convert the total cost to dollars and round to 2 decimal places
    total_cost_dollars = round(total_cost / 100, 2)

    # return the result
    result = total_cost_dollars
    return result

print(solution())