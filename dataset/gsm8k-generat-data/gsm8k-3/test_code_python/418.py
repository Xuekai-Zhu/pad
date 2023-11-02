def solution():
    """Ken had fifty pencils, and he wanted to share some of them with his two friends, Manny and Nilo. Ken gave ten pencils to Manny and ten more pencils to Nilo than he gave to Manny. He kept the rest of the pencils. How many pencils did Ken keep?"""
    # Define the initial number of pencils
    pencils = 50

    # Define the number of pencils Ken gave to Manny
    manny_pencils = 10

    # Define the number of pencils Ken gave to Nilo
    nilo_pencils = manny_pencils + 10

    # Calculate the total number of pencils given away
    total_given = manny_pencils + nilo_pencils

    # Calculate the number of pencils Ken kept
    kept_pencils = pencils - total_given

    # Display the number of pencils Ken kept
    result = kept_pencils
    return result

print(solution())