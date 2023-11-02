def solution():
    """In the fall, 20,000 high school students apply to Harvard University for college. In the spring, 5% of those 20,000 students are accepted to the university. Of the students who are accepted, 90% choose to attend the university, and the other 10% choose to go to other schools. How many students choose to attend Harvard University?"""
    # Define the number of high school students who apply to Harvard University
    applicants = 20000

    # Calculate the number of students accepted to Harvard University
    accepted = applicants * 0.05

    # Calculate the number of accepted students who choose to attend Harvard University
    attending = accepted * 0.9

    # Display the number of students who choose to attend Harvard University
    result = attending
    return result

print(solution())