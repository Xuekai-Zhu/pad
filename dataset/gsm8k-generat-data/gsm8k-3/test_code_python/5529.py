def solution():
    """Angela has half as many insects as Jacob does, and Jacob has 5 times as many insects as Dean. If Dean has 30 insects, how much does Angela have?"""
    # Define the number of insects Dean has
    dean_insects = 30

    # Calculate the number of insects Jacob has
    jacob_insects = dean_insects * 5

    # Calculate the number of insects Angela has
    angela_insects = jacob_insects / 2

    # Display the number of insects Angela has
    result = angela_insects
    return result

print(solution())