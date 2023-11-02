def solution():
    """Wilfred eats 4 carrots on Tuesday and 6 carrots on Wednesday. If Wilfred wants to eat a total of 15 carrots from Tuesday to Thursday, how many carrots does Wilfred need to eat on Thursday?"""
    # Define the number of carrots eaten on Tuesday and Wednesday
    tuesday_carrots = 4
    wednesday_carrots = 6

    # Calculate the number of carrots Wilfred still needs to eat
    remaining_carrots = 15 - (tuesday_carrots + wednesday_carrots)

    # Return the remaining number of carrots to be eaten on Thursday
    result = remaining_carrots
    return result

print(solution())