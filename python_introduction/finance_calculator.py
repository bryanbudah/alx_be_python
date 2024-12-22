monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year (including 5% interest) are: ${projected_annual_savings:.2f}")