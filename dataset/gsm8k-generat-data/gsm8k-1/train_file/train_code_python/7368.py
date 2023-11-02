def solution():
    """Wilfred eats 4 carrots on Tuesday and 6 carrots on Wednesday. If Wilfred wants to eat a total of 15 carrots from Tuesday to Thursday, how many carrots does Wilfred need to eat on Thursday?"""
    total_carrots = 15
    carrots_eaten_tue_wed = 4 + 6
    carrots_left = total_carrots - carrots_eaten_tue_wed
    result = carrots_left
    return result

print(solution())