def solution():
    """Topher, the green giant, wears enormous shoes. The length of one of his shoes is 10 inches longer than 9 times the length of one of Bobby’s shoes. If the length of one of Topher’s shoes is 8-feet and 4-inches, how long, in inches, is one of Bobby’s shoes?"""
    topher_shoe_length_inches = 100  # 8 feet and 4 inches = 100 inches
    bobby_shoe_length = (topher_shoe_length_inches - 10) / 9  # Rearranging equation to solve for Bobby's shoe length
    result = bobby_shoe_length
    return result

print(solution())