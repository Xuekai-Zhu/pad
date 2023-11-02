def solution():
    """Ken had fifty pencils, and he wanted to share some of them with his two friends, Manny and Nilo. Ken gave ten pencils to Manny and ten more pencils to Nilo than he gave to Manny. He kept the rest of the pencils. How many pencils did Ken keep?"""
    # Define the initial number of pencils
    pencils = 50

    # Calculate the number of pencils given to Manny
    pencils_manny = 10

    # Calculate the number of pencils given to Nilo
    pencils_nilo = pencils_manny + 10

    # Calculate the total number of pencils given away
    total_given = pencils_manny + pencils_nilo

    # Calculate the number of pencils Ken kept
    pencils_kept = pencils - total_given

    # return the result
    result = pencils_kept
    return result

print(solution())