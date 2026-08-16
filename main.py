#This is the main file, this file is supposed to be run once and it will call all the required files.

from data_ingestion import load_data
from cagr_calculation import calculate_all_funds_cagr
from cagr_analysis import find_top_performers, find_low_performers
from nav_swing import detect_nav_swing


def print_line(character="-", length=80):
    print(character * length)


def display_cagr_analysis(cagr_results, line_length):
    # Calculate dynamic column width based on the longest fund name
    max_name_len = max(len(result["Fund Name"]) for result in cagr_results)
    name_col_width = max(max_name_len + 3, 55)

    print()
    print("=" * line_length)
    print("CAGR ANALYSIS".center(line_length))
    print("=" * line_length)

    print("\n" + "7-YEAR CAGR")
    
    sorted_results = sorted(
        cagr_results,
        key=lambda x: x["CAGR"],
        reverse=True
    )

    print_line(length=line_length)
    print(f"{'Rank':<6}{'Fund Name':<{name_col_width}}{'CAGR':>10}")
    print_line(length=line_length)

    for rank, result in enumerate(sorted_results, start=1):
        print(
            f"{rank:<6}"
            f"{result['Fund Name']:<{name_col_width}}"
            f"{result['CAGR']:>9.2f}%"
        )

    print_line(length=line_length)

    top_performers = find_top_performers(cagr_results, 2)
    low_performers = find_low_performers(cagr_results, 2)

    print("\nTOP 2 PERFORMING MUTUAL FUNDS")
    print_line(length=line_length)

    for rank, result in enumerate(top_performers, start=1):
        print(
            f"{rank}. {result['Fund Name']}"
            f" - {result['CAGR']:.2f}%"
        )

    print("\nWORST 2 PERFORMING MUTUAL FUNDS")
    print_line(length=line_length)

    for rank, result in enumerate(low_performers, start=1):
        print(
            f"{rank}. {result['Fund Name']}"
            f" - {result['CAGR']:.2f}%"
        )


def display_nav_swings(swings, line_length):
    print()
    print("=" * line_length)
    print("NAV SWING ANALYSIS".center(line_length))
    print("=" * line_length)

    print("\nNAV changes greater than ±5%")
    print_line(length=line_length)

    if not swings:
        print("No NAV swings greater than ±5% were found.")
        return

    current_fund = None

    for swing in swings:

        if swing["Fund Name"] != current_fund:
            current_fund = swing["Fund Name"]

            print()
            print(f"Fund: {current_fund}")
            print_line(length=line_length)

            print(
                f"{'Date':<15}"
                f"{'Previous NAV':>15}"
                f"{'Current NAV':>15}"
                f"{'Change':>12}"
                f"{'Type':>15}"
            )

        date = swing["Date"].strftime("%d-%b-%Y")

        print(
            f"{date:<15}"
            f"{swing['Previous Day NAV']:>15.3f}"
            f"{swing['Current Day NAV']:>15.3f}"
            f"{swing['Percentage Change']:>11.2f}%"
            f"{swing['Swing Type']:>15}"
        )


def display_menu(line_length):
    print()
    print("=" * line_length)
    print("MUTUAL FUND NAV ANALYSIS".center(line_length))
    print("=" * line_length)

    print("\nMAIN MENU")
    print_line(length=line_length)

    print("1. View CAGR Analysis")
    print("2. View NAV Swing Analysis")
    print("3. Exit")

    print_line(length=line_length)


def main():
    filename = input("Enter the NAV data file name: ").strip()

    try:
        data = load_data(filename)
    except FileNotFoundError:
        print("\nError: The specified file was not found.")
        return
    except ValueError as error:
        print(f"\nError: {error}")
        return
    except Exception as error:
        print(f"\nUnexpected error: {error}")
        return

    # Calculate CAGR once after loading the data
    cagr_results = calculate_all_funds_cagr(data)

    # Calculate NAV swings once after loading the data
    nav_swings = detect_nav_swing(data)

    # Calculate consistent line length based on longest fund name
    max_name_len = max(len(result["Fund Name"]) for result in cagr_results)
    name_col_width = max(max_name_len + 3, 55)
    line_length = 6 + name_col_width + 10

    print()
    print("=" * line_length)
    print("MUTUAL FUND NAV ANALYSIS".center(line_length))
    print("=" * line_length)

    print("\nData loaded successfully")
    print(f"Funds found: {data['Fund Name'].nunique()}")
    print(f"NAV records processed: {len(data)}")

    while True:

        display_menu(line_length)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            display_cagr_analysis(cagr_results, line_length)

        elif choice == "2":

            display_nav_swings(nav_swings, line_length)

        elif choice == "3":

            print("\nThank you for using Mutual Fund NAV Analysis.")
            print("Exiting program...")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()