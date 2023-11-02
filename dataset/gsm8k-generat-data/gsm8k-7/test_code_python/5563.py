def solution():
    total_citations = 24
    littering_citations = total_citations / 4   # Littering citations = off-leash dog citations
    parking_citations = littering_citations * 2   # Parking citations = double other citations
    result = littering_citations
    return result

print(solution())