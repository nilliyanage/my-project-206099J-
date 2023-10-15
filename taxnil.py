def calculate_tax(income, tax_rate):
    """
    Calculates tax based on the given income and tax rate.
    """
    tax = income * tax_rate
    return tax

try:
    income = float(input("Enter your income: $"))
    tax_rate = float(input("Enter the tax rate (as a decimal): "))

    tax_amount = calculate_tax(income, tax_rate)
    print("Tax amount: $", tax_amount)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")