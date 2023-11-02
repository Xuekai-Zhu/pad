def solution():
    """Kaylin is five years younger than Sarah, who is twice as old as Eli, who is nine years older than Freyja. If Freyja is ten years old, how old is Kaylin?"""
  
    # Define Freyja's age
    Freyja_age = 10
    
    # Calculate Eli's age
    Eli_age = Freyja_age + 9
    
    # Calculate Sarah's age
    Sarah_age = Eli_age * 2
    
    # Calculate Kaylin's age
    Kaylin_age = Sarah_age - 5
    
    # Display Kaylin's age
    result = Kaylin_age
    return result

print(solution())