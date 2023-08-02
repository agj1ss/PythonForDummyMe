import winreg

# Open the registry key where the software information is stored
software_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                              r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')

# Get the number of subkeys (i.e., installed software)
num_subkeys = winreg.QueryInfoKey(software_key)[0]

# Iterate through the subkeys and print the software information
for i in range(num_subkeys):
    subkey_name = winreg.EnumKey(software_key, i)
    subkey = winreg.OpenKey(software_key, subkey_name)
    try:
        name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
        version = winreg.QueryValueEx(subkey, 'DisplayVersion')[0]
        publisher = winreg.QueryValueEx(subkey, 'Publisher')[0]
        print(f'{name} ({publisher}) - Version {version}')
    except OSError:
        # Some subkeys may not have the required values, ignore them
        pass
    finally:
        subkey.Close()

# Close the software key
software_key.Close()
