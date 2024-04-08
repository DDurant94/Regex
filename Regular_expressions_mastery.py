'''
1. Python Regular Expressions Mastery
Task 1: Code Correction

Problem Statement: You are given a piece of code that is intended to extract email addresses from a given text. 
However, the code contains errors and does not function as expected. Your task is to identify and correct these errors.

Code Example:

<span class="hljs-keyword">import</span> re

text = <span class="hljs-string">"Contact emails are: john.doe@example.com and jane.doe@example.com."</span>
emails = re.findall(<span class="hljs-string">r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"</span>, text)
<span class="hljs-built_in">print</span>(emails)
Expected Outcome:

Correct the regex pattern to capture email addresses effectively.
Modify the code to handle different cases in email addresses.


Task 2: Log File Analysis

Problem Statement: You have a log file represented as a string, containing timestamps and messages. 
Write a script to reformat the timestamps from 'MM-DD-YYYY' to 'YYYY-MM-DD' and anonymize any usernames 
mentioned in the log (format: '@username').

Code Example:

log_data = <span class="hljs-string">"12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."</span>
<span class="hljs-comment"># Your solution here</span>
Expected Outcome:

Correctly reformat the date in each log entry.
Replace all instances of '@username' with '[ANONYMIZED USER]'.
Use re.sub() effectively to achieve the desired text manipulations.

'''
# Task One
# Contact emails are: (.+?)\. grabs everything

import re

text = '<span class="hljs-string">"Contact emails are: john.doe@example.com and jane.doe@example.com."</span>'
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)


# Task Two

# us re.sub to get the text to be replaced
log_data = '<span class="hljs-string">"12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."</span>'

date_change = r"(\d{2})-(\d{2})-(\d{4})"
email_change =r"\@[a-zA-z0-9]+\w"

result = re.sub(date_change,r"\3-\1-\2",log_data) 
results =re.sub(email_change,r"'[ANONYMIZED USER]'",result )
print(results)


  


