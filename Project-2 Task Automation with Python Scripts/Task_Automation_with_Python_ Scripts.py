              # Project- 2 Task Automation with Python Scripts
# Task Extract all email addresses from a .txt file and save them to another file


import re  # Import Module (for pattern matching) 

user_filename = input("Enter file Name: ")

with open (user_filename , "r") as f:
    file_content = f.read()

# Email dhoondhne ke liye ek "pattern" banao 
pattern = r"\w+@\w+\.\w+"  

# ye pattern se match hone wale sab emails ek LIST mein de dega
emails = re.findall(pattern, file_content)


# check list khali hai ya nahi
if emails == []:
    print("No Email Found")
    exit()


with open("output_file.txt" , "w") as f:
    

    for email in emails:
        f.write(f"{email}\n")


print(f"{len(emails)} emails found and saved to output_file.txt")

