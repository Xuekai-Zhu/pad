def solution():
    """A park warden has issued 24 citations over the past three hours. He issued the same number for littering as he did for off-leash dogs, and he issued double the number of other citations for parking fines. How many littering citations did the warden issue?"""
    # Define the total number of citations issued
    total_citations = 24

    # Calculate the number of citations issued for parking fines
    parking_citations = total_citations / 4

    # Calculate the number of citations issued for littering
    littering_citations = total_citations / 8

    # Calculate the number of citations issued for off-leash dogs
    dogs_citations = littering_citations

    result = littering_citations
    return result

print(solution())