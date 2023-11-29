from datetime import datetime, timedelta

def calculate_items(start_date, current_items, current_league, mid_date=None, mid_league=None):
    leagues = {
        '메이저1': 450, '메이저2': 600, '메이저3': 750,
        '올스타1': 900, '올스타2': 1100, '올스타3': 1300,
        '챌린저1': 1500, '챌린저2': 1700, '챌린저3': 1900
    }

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_case1, end_date_case2 = None, None
    bonus_month = None

    while current_items < 20000:
        current_week = current_date.isocalendar()[1]
        current_month = current_date.month

        # Check for mid-date condition
        if mid_date and mid_league and current_date >= datetime.strptime(mid_date, "%Y-%m-%d"):
            current_league = mid_league
            mid_date = None  # Reset mid-date to avoid reapplying the mid-week condition

        weekly_items = leagues[current_league]

        # Apply the bonus condition on the third week of specific months
        if current_week == 3 and current_month in [2, 4, 6, 8, 10, 12] and current_month != bonus_month:
            weekly_items *= 2
            weekly_items += 2000
            bonus_month = current_month

        current_items += weekly_items

        # Update end dates based on conditions
        if current_items >= 10000 and not end_date_case1:
            end_date_case1 = current_date.strftime("%Y-%m-%d")

        if current_items >= 20000 and not end_date_case2:
            end_date_case2 = current_date.strftime("%Y-%m-%d")

        # Move to the next week
        current_date += timedelta(weeks=1)

    return end_date_case1, end_date_case2, bonus_month

# Input values
start_date = input("오늘 날짜 (YYYY-MM-DD): ")
current_items = int(input("현재 아이템 보유 개수: "))
current_league = input("현재 리그 난이도: ")
mid_date = input("중간 날짜 (YYYY-MM-DD, 없으면 Enter): ")
mid_league = input("중간날짜 리그 난이도 (없으면 Enter): ")

# Calculate and print results
end_date_case1, end_date_case2, bonus_month = calculate_items(start_date, current_items, current_league, mid_date, mid_league)

print("\n종료 조건이 충족된 경우:")
print("Case 1: 아이템이 10000개 이상인 경우 -", end_date_case1 if end_date_case1 else "미달성")
print("Case 2: 아이템이 20000개 이상인 경우 -", end_date_case2 if end_date_case2 else "미달성")
print("보너스가 적용된 월:", bonus_month if bonus_month else "적용되지 않음")
