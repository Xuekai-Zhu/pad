def solution():
    """100 people apply for a job at Google. Of the people that apply, only 30% receive interviews. Of those who receive interviews, 20% receive a job offer. Of those who receive a job offer, a third of the people accept the position. How many people accept the position?"""
    applicants = 100
    interview_rate = 0.3
    interviewees = applicants * interview_rate
    job_offer_rate = 0.2
    job_offers = interviewees * job_offer_rate
    accept_rate = 1/3
    accepted_jobs = job_offers * accept_rate
    result = accepted_jobs
    return result

print(solution())