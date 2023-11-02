def solution():
    carrots_eaten = 4 + 6  # Wilfred has already eaten 4 carrots on Tuesday and 6 carrots on Wednesday
    carrots_remaining = 15 - carrots_eaten  # Wilfred wants to eat a total of 15 carrots, so he has carrots_remaining left to eat on Thursday

    required_carrots = carrots_remaining - 4  # Wilfred has already decided to eat 4 carrots on Thursday

    result = required_carrots
    return result

print(solution())