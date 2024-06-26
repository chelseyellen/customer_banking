"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_savings_account = Account(float(balance),0)


    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest = my_savings_account.balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_savings_balance = balance + interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    my_savings_account.set_balance(updated_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    my_savings_account.set_interest(interest)

    # Return the updated balance and interest earned.
    
    # added print functions below to test formulas
    # print(my_account.balance)
    # print(my_account.interest)

    return my_savings_account.balance, my_savings_account.interest

# added execute line below to test the function
# if __name__=="__main__":
#     create_savings_account(10000, 5, 36)