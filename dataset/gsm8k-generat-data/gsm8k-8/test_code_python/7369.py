def solution():
    # Define the number of carrots Wilfred already ate
    tuesday_carrots = 4
    wednesday_carrots = 6

    # Define the total number of carrots Wilfred wants to eat
    total_carrots = 15

    # Calculate the number of carrots Wilfred needs to eat on Thursday
    thursday_carrots = total_carrots - (tuesday_carrots + wednesday_carrots)
    result = thursday_carrots
    return result

print(solution())