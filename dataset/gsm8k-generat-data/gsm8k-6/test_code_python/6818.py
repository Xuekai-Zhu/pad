def solution():
    # Calculate the total number of s'mores needed
    total_s'mores = 15 * 2  # 15 scouts, each need 2 s'mores

    # Calculate the number of chocolate bars needed
    chocolate_bars = (total_s'mores / 3) * 2  # each chocolate bar can make 3 s'mores, each scout needs 2 s'mores

    # Calculate the total cost of the chocolate bars
    cost = chocolate_bars * 1.5  # each chocolate bar costs $1.50

    result = cost
    return result

print(solution())