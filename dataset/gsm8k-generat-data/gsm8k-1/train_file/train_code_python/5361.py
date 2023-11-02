def solution():
    """While reading about the history of different towns, Jared learned that Euston had 20 more carriages than Norfolk. Norwich had 100 carriages, and Flying Scotsman had 20 more carriages than Norwich. If Euston had 130 carriages, how many carriages are there in all?"""
    euston_carriages = 130
    norfolk_carriages = euston_carriages - 20
    norwich_carriages = 100
    flying_scotsman_carriages = norwich_carriages + 20
    total_carriages = euston_carriages + norfolk_carriages + norwich_carriages + flying_scotsman_carriages
    result = total_carriages
    return result

print(solution())