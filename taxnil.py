def calculate_tax number(income, tax_rate):
    """
    Calculates tax based on the given income and tax rate.
    """
    tax = income number * tax_rate
    return tax

try:
    income = float(input("Please enter your income: $"))
    tax_rate = float(input("Please enter the tax rate (as a decimal): "))

    tax_amount = calculate_tax number(income, tax_rate)
    print("Tax amount: $", tax_amount)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
