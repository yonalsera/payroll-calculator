# Payroll Calculator

## Purpose
This is a Python program designed to calculate your salary based on factors like
marital status, hourly pay, and pay period (weekly or monthly). It provides a detailed breakdown on
additional factors such as social security and Medicare to calculate your final paycheck.

## Features
- Calculates **federal taxes** based on 2021 IRS tax brackets for single and married individuals.
- Estimates **state taxes** for all US states.
- Calculates **Social Security** and **Medicare** deductions.
- Supports **weekly** and **monthly** pay periods.
- Interactive user input with validation to prevent incorrect entries.
- Prints a formatted paycheck summary for easy reading.
- Option to **re-enter information**, **print payroll**, or **exit** the program.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/payroll-calculator.git
2. Navigate into your project folder:
   ```bash
   cd payroll-calculator
3. If needed install Python
4. To run Program:
   ```bash
   py payroll_calculator.py
5. Follow the prompts and enter all information accurately.
6. When finished entering, you will be presented with the option to either print,
   re-enter info, or exit the program.
7. Sample Output:
   
        Monthly Pay check of John Doe
        ----------------------------------------
         Employee : John Doe
         Pay Period : Monthly
         Hourly Pay : 60.00
         Marital Status : Married
         State : IL
         Federal Tax : 564.83
         State Tax : 297.00
         Social Security Tax : 372.00
         Medicare Tax : 87.00
        ---------------------------------------
         Initial Pay : 6000.00
         Total Tax : 1320.83
        =======================================
         Final Pay : 4679.17

Notes:
- Federal tax brackets are from IRS Publication 15-T (2021).
- State tax rates are estimated from NerdWallet 2025 state tax rates.
- Social Security is calculated at 6.2%, Medicare at 1.45% of gross pay.
- The program validates all user inputs for accurate calculations.


