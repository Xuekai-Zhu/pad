def solution():
    total_days = 21  # Kelly booked a three week vacation
    days_at_grandparents = 5  # Kelly spent 5 days at her grandparents' house
    days_at_brother = 5  # Kelly spent 5 days at her brother's house
    days_traveling = 4  # Kelly spent 1 day traveling at the beginning, 1 day traveling after visiting grandparents, and 2 days traveling to sister's house and back

    # Calculate the number of days Kelly spent at her sister's house
    days_at_sister = total_days - (days_at_grandparents + days_at_brother + days_traveling + 1)  # Subtracting 1 for the day she spent traveling before visiting her grandparents

    result = days_at_sister
    return result

print(solution())