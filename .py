           
 Function to calculate Simple Interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Function to calculate Compound Interest
def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    ci = amount - p
    return ci

# Main program
def main():
    # Taking inputs from the user
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest (%): "))
    time = float(input("Enter Time (in years): "))

    # Calculating interests
    si = simple_interest(principal, rate, time)
    ci = compound_interest(principal, rate, time)

    # Difference
    diff = ci - si

    # Display results
    print("\n---- Results ----")
    print(f"Simple Interest: {si:.2f}")
    print(f"Compound Interest: {ci:.2f}")
    print(f"Difference (CI - SI): {diff:.2f}")

# Call main function
main()
