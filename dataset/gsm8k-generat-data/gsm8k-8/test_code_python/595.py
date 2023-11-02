def solution():
    # Define the number of bananas Lydia has
    lydia_bananas = 60

    # Calculate the number of bananas Dawn has
    dawn_bananas = lydia_bananas + 40

    # Calculate the total number of bananas Dawn and Lydia have
    dawn_lydia_bananas = lydia_bananas + dawn_bananas

    # Calculate the number of bananas Donna has
    donna_bananas = 200 - dawn_lydia_bananas
    result = donna_bananas
    return result

print(solution())