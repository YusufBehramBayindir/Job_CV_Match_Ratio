import difflib

# Firstly, let's read the keywords from a txt file and store them in a list:
with open('keywords.txt', 'r') as f:
    keywords = f.read().splitlines()

# Then, let's read the job description from another txt file:
with open('job.txt', 'r') as f:
    job_description = f.read()

# Next, let's open the CV file that the user will select:
import PyPDF2

with open('cv.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    cv_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        cv_text += page.extract_text()


# Then, let's clean the keywords and job description text:
import re

# Convert keywords to lowercase and remove unnecessary spaces
keywords = [re.sub(r'\s+', ' ', keyword.strip().lower()) for keyword in keywords]
# Clean job description text by removing unnecessary spaces
job_description = re.sub(r'\s+', ' ', job_description.strip().lower())
# Clean CV text by removing unnecessary spaces
cv_text = re.sub(r'\s+', ' ', cv_text.strip().lower())



# Let's compare the keywords and job description text to calculate the similarity ratio and print the result:
import difflib

# Calculate the similarity ratio between keywords and job description text
match_ratio = difflib.SequenceMatcher(None, ' '.join(keywords), job_description).ratio()

# Calculate the similarity ratio between keywords and the selected CV
match_ratio_cv = difflib.SequenceMatcher(None, ' '.join(keywords), cv_text).ratio()

# Print the result
print(f"Similarity ratio between job description text and keywords: {match_ratio:.2%}")
print(f"Similarity ratio between selected CV and keywords: {match_ratio_cv:.2%}")

print(f"Seçilen CV ile anahtar kelimeler arasındaki benzerlik oranı: {match_ratio_cv:.2%}")
