def solution():
    """A park warden has issued 24 citations over the past three hours. He issued the same number for littering as he did for off-leash dogs, and he issued double the number of other citations for parking fines. How many littering citations did the warden issue?"""
    total_citations = 24
    littering_citations = total_citations // 4
    result = littering_citations
    return result

print(solution())