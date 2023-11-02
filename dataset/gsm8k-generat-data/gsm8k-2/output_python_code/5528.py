def solution():
    """Angela has half as many insects as Jacob does, and Jacob has 5 times as many insects as Dean. If Dean has 30 insects, how much does Angela have?"""
    dean_insects = 30
    jacob_insects = 5 * dean_insects
    angela_insects = jacob_insects / 2
    result = angela_insects
    return result

print(solution())