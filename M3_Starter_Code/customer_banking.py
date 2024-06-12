# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is the starting balance for the savings account? "))
    savings_interest = float(input("What is the interest rate on the savings account? "))
    savings_maturity = int(input("How many months will this savings account be active? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned on the savings account is ${savings_interest_earned: ,.2f} with an updated total balance of ${updated_savings_balance: ,.2f} across {savings_maturity} months.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("What is the starting balance of the cd account? "))
    cd_interest = float(input("What is the interest rate on the cd account? "))
    cd_maturity = int(input("What is the maturity period for the cd account? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned on the cd account is ${cd_interest_earned: ,.2f} with an updated total balance of ${updated_cd_balance: ,.2f} across {cd_maturity} months.")


if __name__ == "__main__":
    # Call the main function.
    main()