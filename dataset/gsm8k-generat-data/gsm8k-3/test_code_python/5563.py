def solution():
    """A park warden has issued 24 citations over the past three hours. He issued the same number for littering as he did for off-leash dogs, and he issued double the number of other citations for parking fines. How many littering citations did the warden issue?"""
    # Define the number of citations for each type of violation
    littering_citations = 0
    off_leash_citations = 0
    parking_citations = 0

    # Find the number of citations for each type of violation
    off_leash_citations = 24 / 2
    parking_citations = off_leash_citations / 2
    littering_citations = off_leash_citations

    # Display the number of littering citations
    result = littering_citations
    return result

print(solution())