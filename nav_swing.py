#To detect NAV changes greater than +5% and - %5

def detect_nav_swing(df):

    swings = []

    for fund_name, group in df.groupby("Fund Name"):
        group = group.sort_values("Date").copy()

        previous_day_nav = None

        for _, row in group.iterrows():
            current_day_nav = row["NAV"]

            if previous_day_nav is None:
                previous_day_nav = current_day_nav
                continue

            percent_change = ((current_day_nav - previous_day_nav) / previous_day_nav) * 100

            if percent_change > 5 or percent_change < (-5):
                swings.append({
                    "Fund Name": fund_name,
                    "Date": row["Date"],
                    "Previous Day NAV": previous_day_nav,
                    "Current Day NAV": current_day_nav,
                    "Percentage Change": percent_change,
                    "Swing Type": "Increase" if percent_change > 5 else "Decrease"
                })
            
            previous_day_nav = current_day_nav

    return swings


