def solution():
    """Adrianne is collecting different kinds of beads for making bracelets. Her mother gave her 20 metallic beads. Her sister gave her ten more beads than her mother, and her friend gave her twice as many as her mother gave. How many beads did Adrianne have altogether?"""
    mother = 20
    sister = mother + 10
    friend = mother * 2
    total_beads = mother + sister + friend
    result = total_beads
    return result

print(solution())