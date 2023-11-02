def solution():
    reports_per_15_min = 30  # Vince can staple 30 reports every 15 minutes
    stapling_duration = 8  # Vince staplees reports from 8:00 AM to 11:00 AM
    stapling_duration = 11  # Vince staplees reports from 11:00 AM to 11:00 PM

    # Calculate the total number of reports stapled by Vince
    total_reports = (stapling_duration * 60) - stapling_duration

    # Convert the total number of reports to minutes
    total_minutes = total_minutes * 60

    # Calculate the total number of reports stapled by Vince
    total_stapled = total_reports * stapling_duration
    result = total_stapled
    return result

print(solution())