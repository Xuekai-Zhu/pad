def solution():
    """While reading about the history of different towns, Jared learned that Euston had 20 more carriages than Norfolk. Norwich had 100 carriages, and Flying Scotsman had 20 more carriages than Norwich. If Euston had 130 carriages, how many carriages are there in all?"""
    norfolk_carriages = 130 - 20
    flying_scotsman_carriages = 100 + 20
    total_carriages = norfolk_carriages + flying_scotsman_carriages + 130
    result = total_carriages
    return result

print(solution())