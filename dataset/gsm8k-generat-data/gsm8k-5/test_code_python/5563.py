def solution():
    total_citations = 24  # The park warden issued 24 citations over the past three hours
    littering_citations = total_citations / 4  # Littering citations were the same as off-leash dog citations, so each was a quarter of the total
    parking_citations = 2 * littering_citations  # Parking citations were twice the number of other citations, which were the same as littering and off-leash dog citations combined
    result = littering_citations
    return result

print(solution())