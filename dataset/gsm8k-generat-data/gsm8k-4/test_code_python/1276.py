def solution():
    """Kaylin is five years younger than Sarah, who is twice as old as Eli, who is nine years older than Freyja. If Freyja is ten years old, how old is Kaylin?"""
    
    # Assigning age of Freyja to variable age_freyja
    age_freyja = 10
    
    # Coverting age of Freyja to variable age_eli
    age_eli = age_freyja + 9
    
    # Coverting age of Eli to variable age_sarah
    age_sarah = age_eli * 2
    
    # Coverting age of Sarah to variable age_kaylin
    age_kaylin = age_sarah - 5
    
    # Storing the age of Kaylin in result
    result = age_kaylin
    return result

print(solution())