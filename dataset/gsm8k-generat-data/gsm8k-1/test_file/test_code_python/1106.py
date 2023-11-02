def solution():
    """Although Soledad works in a windowless office, she loves the outdoors. She will be on vacation for the entire month of June and cannot wait to hike 9,300 miles within that month. She is thinking of walking twice a day, covering 125 miles each time. How many more miles per day must Soledad hike to complete her journey on time?"""
    total_miles = 9300
    miles_per_day = (125 * 2) # hike twice a day
    days_in_june = 30
    days_to_complete = total_miles / miles_per_day
    additional_miles_per_day = (total_miles / days_in_june) - miles_per_day
    result = additional_miles_per_day
    return result

Note: There is no solution provided for the Samantha's last name question as it's not a math problem and requires additional context and information.

print(solution())