def solution():
    '''
    Freddy is calling his family on New Year's Eve. He calls his dad, who lives in the same city as him, 
    and they talk for 45 minutes. Then he calls his brother, who lives on the other side of the world, 
    and they talk for 31 minutes. Local calls cost 5 cents a minute, while international calls cost 
    25 cents a minute. How many dollars did Freddy spend calling his family on New Year's Eve?
    '''

    # Calculate the cost of the call to his dad
    dad_call_cost = 45 * 0.05

    # Calculate the cost of the call to his brother
    brother_call_cost = 31 * 0.25

    # Calculate the total cost of the calls
    total_cost = dad_call_cost + brother_call_cost

    # Display the total cost in dollars
    result = total_cost / 100
    return result

print(solution())