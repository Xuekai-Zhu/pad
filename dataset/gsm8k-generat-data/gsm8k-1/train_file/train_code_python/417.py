def solution():
    """Ken had fifty pencils, and he wanted to share some of them with his two friends, Manny and Nilo.
    Ken gave ten pencils to Manny and ten more pencils to Nilo than he gave to Manny.
    He kept the rest of the pencils. How many pencils did Ken keep?"""
    total_pencils = 50
    manny_pencils = 10
    nilo_pencils = manny_pencils + 10
    pencils_given = manny_pencils + nilo_pencils
    pencils_kept = total_pencils - pencils_given
    result = pencils_kept
    return result

print(solution())