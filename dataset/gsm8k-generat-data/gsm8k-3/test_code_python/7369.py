def solution():
    """Wilfred eats 4 carrots on Tuesday and 6 carrots on Wednesday. If Wilfred wants to eat a total of 15 carrots from Tuesday to Thursday, how many carrots does Wilfred need to eat on Thursday?"""
    # Calculate the total number of carrots Wilfred has eaten on Tuesday and Wednesday
    total_eaten = 4 + 6

    # Calculate how many carrots Wilfred needs to eat on Thursday to reach his goal
    carrots_left = 15 - total_eaten
    carrots_on_thursday = carrots_left

    # Display how many carrots Wilfred needs to eat on Thursday
    result = carrots_on_thursday
    return result

print(solution())