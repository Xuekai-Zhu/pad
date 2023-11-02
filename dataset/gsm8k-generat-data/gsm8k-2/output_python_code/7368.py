def solution():
    """Wilfred eats 4 carrots on Tuesday and 6 carrots on Wednesday. If Wilfred wants to eat a total of 15 carrots from Tuesday to Thursday, how many carrots does Wilfred need to eat on Thursday?"""
    tuesday_carrots = 4
    wednesday_carrots = 6
    total_carrots = 15
    thursday_carrots = total_carrots - tuesday_carrots - wednesday_carrots
    result = thursday_carrots
    return result

print(solution())