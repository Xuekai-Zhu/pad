def solution():
    """Janet works as an exterminator and she also sells molten metal casts of fire ant nests on the Internet. Janet gets paid $70 an hour for exterminator work and makes $20/pound on her ant nest sculptures. If she does 20 hours of exterminator work and sells a 5-pound sculpture and a 7-pound sculpture, how much money does she make?"""
    # Calculate the earnings from exterminator work
    exterminator_earnings = 70 * 20

    # Calculate the earnings from selling sculptures
    sculpture_earnings = (5 + 7) * 20

    # Calculate the total earnings
    total_earnings = exterminator_earnings + sculpture_earnings

    result = total_earnings
    return result

print(solution())