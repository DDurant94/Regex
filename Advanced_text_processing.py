'''
3. Advanced Text Processing with Python Regex
Objective:
The goal of this assignment is to harness the full potential of Python's Regular Expressions for advanced text processing. 
You'll tackle complex tasks involving data extraction, validation, and transformation, sharpening your skills in applying 
regex in various challenging scenarios.

Task 1: Advanced Data Extraction

Problem Statement:
Develop a script to extract specific information from a formatted text. The text contains data entries delimited by 
semicolons and formatted as 'Key: Value'. Extract the value corresponding to a specific key.

Code Example:

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here
Expected Outcome:

Successfully extract the 'Occupation' value from the text.
Implement a regex pattern that accurately targets and captures the desired data.
Task 2: URL Validator

Problem Statement:
Write a Python program to validate a list of URLs. A valid URL should start with 'http://' or 'https://', followed by a domain name.

Code Example:

urls = ["https://example.com", "www.example.com", "http://test.com"]
# Validate each URL in the list
# Your code here
Expected Outcome:

Correctly identify and categorize valid and invalid URLs from the list.
Use regex to validate the format of each URL.
'''

import re

# Task one


def customer_occupation(text):
  # Need to put where the text i want starts and ends to get a value returned
  occupation_extraction = r"Occupation: (.*?);"
  occupation = re.search(occupation_extraction,text)
  if occupation:
    stored_info = occupation.group(1)
    print(stored_info)



text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
customer_occupation(text)

# Task two


  


def processing_domains(urls):
  url_perimeters = r"^(https://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$|^(http://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  valid_domain = []
  invalid_domain = []
  try:
      for url in urls:
        matches = re.search(url_perimeters,url)
        if matches:
          valid_domain.append(url)
        else:
          invalid_domain.append(url)
  except Exception as e:
      print(f"Error: Problem with {url}: {e}")
  return valid_domain , invalid_domain


urls = ["https://example.com", "www.example.com", "http://test.com"]

valid,invalid = processing_domains(urls)
print(f"Valid Emails: {valid}")
print(f"Invalid Emails: {invalid}")