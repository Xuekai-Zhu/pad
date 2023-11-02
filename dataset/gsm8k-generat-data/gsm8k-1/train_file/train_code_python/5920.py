def solution():
    """Freddy is calling his family on New Year's Eve. He calls his dad, who lives in the same city as him, and they talk for 45 minutes. Then he calls his brother, who lives on the other side of the world, and they talk for 31 minutes. Local calls cost 5 cents a minute, while international calls cost 25 cents a minute. How many dollars did Freddy spend calling his family on New Year's Eve?"""
    local_call_cost = 0.05
    international_call_cost = 0.25
    dad_call_duration = 45
    brother_call_duration = 31
    total_dad_call_cost = dad_call_duration * local_call_cost
    total_brother_call_cost = brother_call_duration * international_call_cost
    total_cost = total_dad_call_cost + total_brother_call_cost
    result = total_cost
    return result

print(solution())