import re  # Import regular expressions module

#function to validate a US phone number
def validate_phone_number(phone):
    """
    Validates a US phone number.
    Acceptable formats:
    - 123-456-7890
    - (123) 456-7890
    - 1234567890
    - 123.456.7890
    - +1 123 456 7890
    """
    pattern = r'^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$'
    if re.match(pattern, phone):
        return True
    else:
        return False

# to validate a US Social Security Number (SSN)
def validate_ssn(ssn):
    """
    Validates a US Social Security Number.
    Acceptable format:
    - 123-45-6789
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(pattern, ssn):
        return True
    else:
        return False

# to validate a US ZIP Code
def validate_zip(zip_code):
    """
    Validates a US ZIP Code.
    Acceptable formats:
    - 12345
    - 12345-6789
    """
    pattern = r'^\d{5}(-\d{4})?$'
    if re.match(pattern, zip_code):
        return True
    else:
        return False

#main function to get input and display results
def main():
    #get user input for phone number, SSN, and ZIP Code
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (SSN): ")
    zip_code = input("Enter a ZIP Code: ")

    # phone number
    if validate_phone_number(phone):
        print("✅ Phone number is valid.")
    else:
        print("❌ Phone number is invalid.")

    # SSN
    if validate_ssn(ssn):
        print("✅ SSN is valid.")
    else:
        print("❌ SSN is invalid.")

    # ZIP Code
    if validate_zip(zip_code):
        print("✅ ZIP Code is valid.")
    else:
        print("❌ ZIP Code is invalid.")

if __name__ == "__main__":
    main()