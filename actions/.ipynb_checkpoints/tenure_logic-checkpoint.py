def calculate_monthly_installment(principal, tenure, rate):
    """Calculates monthly EMI based on principal, tenure, and interest rate."""
    rate = rate / (12 * 100)  # Monthly interest rate
    emi = (principal * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)
    return round(emi, 2)


