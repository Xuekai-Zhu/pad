def solution():
    total_citations = 24
    parking_citations = total_citations / 2
    other_citations = total_citations - parking_citations
    littering_citations = other_citations / 2
    result = littering_citations
    return result

print(solution())