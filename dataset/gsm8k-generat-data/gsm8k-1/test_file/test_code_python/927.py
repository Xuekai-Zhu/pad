def solution():
    """The combined age of Peter, Paul and Jean is 100 years old. Find the age of Peter knowing that Paul is 10 years older than John and that Peter’s age is equal to the sum of Paul and John's age."""
    combined_age = 100
    paul_age = 0
    john_age = 0
    peter_age = 0
    
    # Try different possibilities for Paul's age until we find the correct ages for all three
    for i in range(1, 50):
        paul_age = i
        john_age = paul_age - 10
        peter_age = paul_age + john_age
        
        if peter_age + paul_age + john_age == combined_age:
            break
    
    result = peter_age
    return result

print(solution())