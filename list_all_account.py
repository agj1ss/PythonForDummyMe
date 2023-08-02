import wmi

# Connect to WMI namespace
c = wmi.WMI()

# Query for user accounts
users = c.Win32_UserAccount()

# Query for Administrators accounts
admin = None
for group in c.Win32_Group():
    if group.Name == "Administrators":
        admin = [a.Name for a in group.associators(wmi_result_class="Win32_UserAccount")]

# Print out user account information
for user in users:
    print(">>>  Name: ", user.Name)
    print("     Administrator: ", (user.Name in admin))
    print("     Disable: ", user.Disabled)
    print("     Local: ", user.LocalAccount)
    print("     Password Changeable: ", user.PasswordChangeable)
    print("     Password Expires: ", user.PasswordExpires)
    print("     Password Required: ", user.PasswordRequired)
    print("     Account Type: ", user.AccountType)
    print("     Local Account: ", user.LocalAccount)
    print("     Description: ", user.Description)
    print("\n")
