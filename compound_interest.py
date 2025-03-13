def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.

    :param principal: Initial amount of money
    :param rate: Annual interest rate (in decimal)
    :param time: Time the money is invested for (in years)
    :param n: Number of times interest is compounded per year
    :return: Compound interest
    """
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

# Example usage
principal = 1000  # Initial amount
rate = 0.05  # Annual interest rate of 5%
time = 10  # Invested for 10 years
n = 4  # Interest is compounded quarterly

ci = calculate_compound_interest(principal, rate, time, n)
print(f"The compound interest is: {ci:.2f}")
