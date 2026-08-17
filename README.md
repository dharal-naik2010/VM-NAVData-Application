# 📈 Mutual Fund NAV Analysis Tool

Welcome! This repository houses a clean, modular, and human-friendly command-line Python application developed to ingest, validate, and analyze mutual fund Net Asset Value (NAV) data. 

This project was built as a solution for the **Mutual Fund NAV Analysis Programming Assessment**. It focuses on clean code structure, error handling, and a highly polished terminal-based dashboard.

---

## 📁 Project Structure

Instead of bundling everything into one complex file, this application is built with modularity in mind. Each script has a single responsibility:

```text
VM-NAVData-Application/
│
├── main.py                # App entry point, menu orchestration, and terminal rendering
├── data_ingestion.py      # Parses/loads and validates CSV and Excel data files
├── cagr_calculation.py    # Computes CAGR for individual and all mutual funds
├── cagr_analysis.py       # Identifies top and bottom performing mutual funds
├── nav_swing.py           # Detects day-to-day price movements > ±5%
│
├── requirements.txt       # Project dependencies (pandas, openpyxl)
├── .gitignore             # Configured to ignore virtual environments and Python cache files
└── README.md              # Human-friendly documentation
```

---

## 🛠️ Module Breakdown

Here's a breakdown of what happens under the hood:

*   [`main.py`]: **The Command Center.** Manages the main application loop, takes user inputs, and prints the dynamically aligned terminal interface.
*   [`data_ingestion.py`]: **The Gatekeeper.** Safely loads CSV or Excel files using Pandas, validates the file structure, and cleans up dates and numeric columns.
*   [`cagr_calculation.py`]: **The Calculator.** Computes the Compound Annual Growth Rate (CAGR) based on the exact number of days between the first and last dates in the dataset.
*   [`cagr_analysis.py`]: **The Analyst.** Ranks mutual funds by performance to extract the top-performing and worst-performing funds.
*   [`nav_swing.py`]: **The Sentinel.** Scans through the dates for each fund chronologically and triggers an alert if the day-to-day NAV changes by more than $\pm 5\%$.

---

## 📋 Features & Implementation Details

Here is how each task from the assessment is addressed:

### 1. Data Ingestion & Strict Validation (Task 1 & 2)
The application accepts both `.csv` and `.xlsx` files. The ingestion module ensures the dataset contains exactly three columns:
*   `Fund Name` (String)
*   `Date` (Parsed into datetime objects)
*   `NAV` (Converted to float)

If a column is missing or named incorrectly, the program stops immediately and displays a clear error message instead of crashing.

### 2. Precise CAGR Analysis (Task 3.1 & 3.2)
To calculate the compound annual growth rate over the 7-year period, we use the following standard formula:

```text
CAGR = ((Ending NAV / Beginning NAV) ^ (1 / Years)) - 1
```

Where:
*   `Years = (Ending Date - Beginning Date) in days / 365.25` (using `365.25` ensures leap years are accounted for).
*   The application automatically ranks all mutual funds and displays the **Top 2** and **Worst 2** performing funds.

### 3. Smart Day-to-Day NAV Swing Detection (Task 3.3)
Instead of matching arbitrary calendar days, the swing detection algorithm groups records by fund and sorts them chronologically. It compares each day's NAV with the **previous available trading day's** NAV. If the change exceeds $\pm 5\%$, it logs:
*   The Date
*   The exact percentage change (Increase/Decrease)
*   The previous vs. new price for context

### 4. Dynamic Console Dashboard (Bonus UX Feature)
Different mutual funds have vastly different name lengths. Hardcoded column widths make the output look cluttered or wrap lines awkwardly. This application dynamically measures the longest fund name in your dataset and adjusts the column widths and line breaks of the console UI so it aligns perfectly every time.

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites
Make sure you have **Python 3.9** (or higher) installed.

### 1. Set Up a Virtual Environment
Isolate project dependencies by creating a python virtual environment:

```bash
# Navigate to the project folder
cd VM-NAVData-Application

# Create the virtual environment
python3 -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Or activate it (Windows PowerShell)
.venv\Scripts\activate
```

### 2. Install Dependencies
Install the required packages (`pandas` and `openpyxl` for Excel ingestion):

```bash
pip install -r requirements.txt
```

### 3. Add Your Data
Ensure your data file (e.g., `NAV_Data.xlsx` or `NAV_Data.csv`) is placed in the project root folder. (A sample `NAV_Data.xlsx` containing a 7-year history for 5 AMFI funds is already included in this repository!).

---

## 🎮 How to Run

Run the main file:
```bash
python main.py
```

### Program Walkthrough & CLI Preview

When you launch the program and load the sample dataset, you will see the following interactive workflow:

1. **Ingest your file:**
   ```text
   Enter the NAV data file name: NAV_Data.xlsx

   =====================================================================================
                                  MUTUAL FUND NAV ANALYSIS                              
   =====================================================================================

   Data loaded successfully
   Funds found: 5
   NAV records processed: 8647
   ```

2. **The Main Menu:**
   ```text
   =====================================================================================
                                  MUTUAL FUND NAV ANALYSIS                              
   =====================================================================================

   MAIN MENU
   -------------------------------------------------------------------------------------
   1. View CAGR Analysis
   2. View NAV Swing Analysis
   3. Exit
   -------------------------------------------------------------------------------------
   Enter your choice: 
   ```

3. **Option 1: CAGR Performance Summary**
   ```text
   =====================================================================================
                                       CAGR ANALYSIS                                    
   =====================================================================================

   7-YEAR CAGR
   -------------------------------------------------------------------------------------
   Rank  Fund Name                                                                  CAGR
   -------------------------------------------------------------------------------------
   1     HDFC Flexi Cap Fund - Growth Plan                                        18.94%
   2     ICICI Prudential Large Cap Fund (erstwhile Bluechip Fund) - Growth       15.65%
   3     Motilal Oswal Flexi Cap Fund Regular Plan-Growth Option                  14.84%
   4     SBI Large Cap FUND-REGULAR PLAN GROWTH                                   14.25%
   5     Axis Large Cap Fund - Regular Plan - Growth                              11.37%
   -------------------------------------------------------------------------------------

   TOP 2 PERFORMING MUTUAL FUNDS
   -------------------------------------------------------------------------------------
   1. HDFC Flexi Cap Fund - Growth Plan - 18.94%
   2. ICICI Prudential Large Cap Fund (erstwhile Bluechip Fund) - Growth - 15.65%

   WORST 2 PERFORMING MUTUAL FUNDS
   -------------------------------------------------------------------------------------
   1. Axis Large Cap Fund - Regular Plan - Growth - 11.37%
   2. SBI Large Cap FUND-REGULAR PLAN GROWTH - 14.25%
   ```

4. **Option 2: NAV Daily Swings Alert**
   ```text
   =====================================================================================
                                     NAV SWING ANALYSIS                                 
   =====================================================================================

   NAV changes greater than ±5%
   -------------------------------------------------------------------------------------

   Fund: Axis Large Cap Fund - Regular Plan - Growth
   -------------------------------------------------------------------------------------
   Date              Previous NAV    Current NAV      Change           Type
   20-Sep-2019             28.560         30.100       5.39%       Increase
   12-Mar-2020             30.440         28.700      -5.72%       Decrease
   16-Mar-2020             29.400         27.790      -5.48%       Decrease
   18-Mar-2020             27.180         25.690      -5.48%       Decrease
   23-Mar-2020             26.290         23.480     -10.69%       Decrease
   25-Mar-2020             24.110         25.410       5.39%       Increase
   07-Apr-2020             24.520         26.210       6.89%       Increase
   ```