'''
4. Python Regex Challenge: Enhancing E-Commerce Operations
Objective:

This assignment aims to refine your skills in using Python Regular Expressions to address common challenges 
in e-commerce operations. You will focus on tasks such as product categorization, customer review analysis, 
and data formatting, crucial for efficient e-commerce management.

Task 1: Product Description Keyword Tagging

Problem Statement:
You have a list of product descriptions. Your task is to tag each product based on keywords in the description. 
For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.

Code Example:

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# Tag each product based on keywords in the description
# Your code here
Expected Outcome:

Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen') using regex to 
identify relevant keywords.
Use regex to match specific product-related keywords in each description.
Task 2: Pricing Format Standardization

Problem Statement:
You have a string containing various price formats from an international e-commerce site. 
Standardize all prices to the format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

Code Example:

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
# Standardize all prices to 'USD XX.XX' format
# Your code here
Expected Outcome:

Convert all price formats in the string to a standardized 'USD XX.XX' format.
Use re.sub() to perform the necessary replacements and format transformations.
'''

import re

# Task one
def sorting_products(description):
  categories_to_sort = {'Electronics':r"\b(Smartphone|screen)\b",
                        'Apparel':r"\b(Cotton|size)\b",
                        'Home & Kitchen':r"\b(kitchen|knife)\b"
                        }
  for category,sorting_code in  categories_to_sort.items():
    #take our regex sort to see if we have a match and if we do we return that category 
    if re.search(sorting_code,description,re.IGNORECASE):
      return category
  return "General"

def organize_products(descriptions):
# make an empty dict to store our sorted values in right categories
  organized_category = {'Electronics':[],'Apparel':[],'Home & Kitchen':[],"General":[]}
  for description in descriptions:
    try:
      # loop the list and pass each description into a function to use regex for sorting 
      category = sorting_products(description)
      # append the description to the category our function returns 
      organized_category[category].append(description)
    except Exception as e:
      print(f"Error sorting descriptions: {description} {e}")
      # use this general as a catch all for no matches 
      organized_category["General"].append(description)
  return organized_category
      
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# split the dict down to see it
descriptions_organized = organize_products(descriptions)
for category, description in descriptions_organized.items():
  print(f"{category}: {description}")





# Task two

# take the numbers (XX.XX) from the string and return the numbers in the format of (USD XX.XX)

# I can't figure out why I can't get the extra space to go away after the cost. If i make the USD flush I have 2 other problems
def standardize_prices(price_data):
  # need to match before ? and after ?
  standard_money =r"(\$|USD)?\s?(\d+\.\d{2})\s?(USD|\$)?"
  usd_data = re.sub(standard_money,r" USD \2", price_data)
  return usd_data


price_data = "Items cost $15.99, 20.00 USD, and 7.50$."

result = standardize_prices(price_data)
print(result)
