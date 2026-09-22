import gradio as gr


# ==============================
# Bank Account Class
# ==============================

class BankAccount:

    # Class Attribute
    account_count = 0

    def __init__(self, name, email, balance):
        # Instance Attributes
        self.name = name
        self.email = email
        self._balance = balance

        # Increase total accounts
        BankAccount.account_count += 1

    # Property Getter
    @property
    def balance(self):
        return self._balance

    # Deposit Method
    def deposit(self, amount):

        if amount <= 0:
            return "❌ Deposit amount must be greater than 0."

        self._balance += amount

        return (
            f"✅ ${amount:.2f} deposited successfully.\n"
            f"Current balance: ${self.balance:.2f}"
        )

    # Withdraw Method
    def withdraw(self, amount):

        if amount <= 0:
            return "❌ Withdrawal amount must be greater than 0."

        if amount > self._balance:
            return (
                f"❌ Insufficient balance.\n"
                f"Current balance: ${self.balance:.2f}"
            )

        self._balance -= amount

        return (
            f"✅ ${amount:.2f} withdrawn successfully.\n"
            f"Current balance: ${self.balance:.2f}"
        )

    # Display Method
    def display_account(self):

        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Balance: ${self.balance:.2f}"
        )


# ==============================
# Store Accounts
# ==============================

accounts = []


# ==============================
# Create Account
# ==============================

def create_account(name, email, balance):

    if not name or not email:
        return "❌ Name and email are required."

    if balance is None:
        return "❌ Please enter an initial balance."

    if balance < 0:
        return "❌ Initial balance cannot be negative."

    account = BankAccount(
        name=name,
        email=email,
        balance=balance
    )

    accounts.append(account)

    return (
        "✅ Account created successfully!\n\n"
        f"Name: {account.name}\n"
        f"Email: {account.email}\n"
        f"Balance: ${account.balance:.2f}"
    )


# ==============================
# Show Accounts
# ==============================

def show_accounts():

    if len(accounts) == 0:
        return "❌ No accounts found.\nPlease create an account first."

    result = ""

    for index, account in enumerate(accounts, start=1):

        result += (
            f"===== Account {index} =====\n"
            f"{account.display_account()}\n\n"
        )

    return result


# ==============================
# Get Account
# ==============================

def get_account(account_number):

    if len(accounts) == 0:
        return None, "❌ No accounts found. Please create an account first."

    if account_number is None:
        return None, "❌ Please enter an account number."

    account_number = int(account_number)

    if account_number < 1 or account_number > len(accounts):
        return None, "❌ Invalid account number."

    return accounts[account_number - 1], None


# ==============================
# Deposit Money
# ==============================

def deposit_money(account_number, amount):

    account, error = get_account(account_number)

    if error:
        return error

    if amount is None:
        return "❌ Please enter an amount."

    return account.deposit(amount)


# ==============================
# Withdraw Money
# ==============================

def withdraw_money(account_number, amount):

    account, error = get_account(account_number)

    if error:
        return error

    if amount is None:
        return "❌ Please enter an amount."

    return account.withdraw(amount)


# ==============================
# Number of Accounts
# ==============================

def show_account_count():

    return f"Total Accounts: {BankAccount.account_count}"


# ==============================
# Gradio Interface
# ==============================

with gr.Blocks(title="Simple Bank System") as app:

    gr.Markdown(
        """
        # 🏦 Simple Bank System

        A simple banking application built with **Python OOP + Gradio**
        """
    )

    # --------------------------------
    # Create Account Tab
    # --------------------------------

    with gr.Tab("Create Account"):

        gr.Markdown("## Create a New Account")

        name_input = gr.Textbox(
            label="Name",
            placeholder="Enter your name"
        )

        email_input = gr.Textbox(
            label="Email",
            placeholder="Enter your email"
        )

        balance_input = gr.Number(
            label="Initial Balance",
            minimum=0
        )

        create_button = gr.Button(
            "Create Account",
            variant="primary"
        )

        create_output = gr.Textbox(
            label="Result",
            lines=6
        )

        create_button.click(
            fn=create_account,
            inputs=[
                name_input,
                email_input,
                balance_input
            ],
            outputs=create_output
        )

    # --------------------------------
    # Accounts Tab
    # --------------------------------

    with gr.Tab("Accounts"):

        gr.Markdown("## All Accounts")

        show_accounts_button = gr.Button(
            "Show All Accounts"
        )

        accounts_output = gr.Textbox(
            label="Accounts",
            lines=15
        )

        show_accounts_button.click(
            fn=show_accounts,
            inputs=[],
            outputs=accounts_output
        )

        count_button = gr.Button(
            "Show Number of Accounts"
        )

        count_output = gr.Textbox(
            label="Total Accounts"
        )

        count_button.click(
            fn=show_account_count,
            inputs=[],
            outputs=count_output
        )

    # --------------------------------
    # Transactions Tab
    # --------------------------------

    with gr.Tab("Transactions"):

        gr.Markdown("## Deposit / Withdraw")

        account_number_input = gr.Number(
            label="Account Number",
            minimum=1,
            precision=0
        )

        amount_input = gr.Number(
            label="Amount",
            minimum=0
        )

        with gr.Row():

            deposit_button = gr.Button(
                "Deposit Money"
            )

            withdraw_button = gr.Button(
                "Withdraw Money"
            )

        transaction_output = gr.Textbox(
            label="Transaction Result",
            lines=5
        )

        deposit_button.click(
            fn=deposit_money,
            inputs=[
                account_number_input,
                amount_input
            ],
            outputs=transaction_output
        )

        withdraw_button.click(
            fn=withdraw_money,
            inputs=[
                account_number_input,
                amount_input
            ],
            outputs=transaction_output


        )


# ==============================
# Run Application
# ==============================

app.launch()