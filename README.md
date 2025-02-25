# Fee Management System

## Overview

This project is a simple fee management system that allows an administrator to:

- Authenticate using an OTP-based login system.
- Edit user fee payment status.
- Send emails to users with pending fees.
- Send emails to users who have cleared their fees.

## Features

- **OTP Authentication:** Sends a one-time password (OTP) to the admin's email for login validation.
- **User Management:** Allows the admin to update the fee status of users.
- **Email Notifications:** Sends fee pending or fee cleared notifications via email.

## Files in the Project

1. **otp.py** - Handles OTP generation and sending via email.
2. **feepaid.py** - Sends emails to users who have cleared their fees.
3. **feepending.py** - Sends emails to users with pending fees.
4. **main.py** - The main script that manages user interactions and email notifications.

## Prerequisites

- Python 3.x
- An active Gmail account for sending emails
- `smtplib` and `email` libraries (included in Python standard library)

## Setup Instructions

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/fee-management-system.git
   ```

2. Navigate to the project directory:

   ```sh
   cd fee-management-system
   ```

3. Update the email credentials in `otp.py`, `feepaid.py`, and `feepending.py`:

   - Replace `xxxxxxxxxx@gmail.com` with your Gmail address.
   - Replace `xxxx xxxx xxxx xxxx` with your app-specific password.

4. Run the main script:

   ```sh
   python main.py
   ```

## Usage

1. Enter the admin username (`admin`).
2. Enter the OTP received in your email.
3. Select an option from the menu:
   - Edit user fee status
   - Send emails to users with pending fees
   - Send emails to users who have cleared their fees
4. Follow the on-screen instructions.

## Notes

- Ensure that **Less Secure Apps** access is enabled for your Gmail account or use an **App Password**.
- Modify `userdetails` in `main.py` to include real user information.

