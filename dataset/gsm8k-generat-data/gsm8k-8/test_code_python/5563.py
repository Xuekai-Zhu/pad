def solution():
    # Define the total number of citations issued
    total_citations = 24

    # Calculate the number of citations issued for parking fines
    parking_citations = total_citations / 3 * 2

    # Calculate the number of citations issued for littering and off-leash dogs
    littering_citations = (total_citations - parking_citations) / 2

    result = littering_citations
    return result

print(solution())