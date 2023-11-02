def solution():
    food_budget = 100 * 4  # Celia plans to spend $100 a week on food for four weeks
    rent = 1500  # Celia will spend $1500 on rent
    video_streaming = 30  # Celia will spend $30 on video streaming services
    cell_phone = 50  # Celia will spend $50 on cell phone usage

    # Calculate Celia's total spending for the month
    total_spending = food_budget + rent + video_streaming + cell_phone

    # Calculate how much Celia will put into savings
    savings = total_spending * 0.1
    result = savings
    return result

print(solution())