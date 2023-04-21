import difflib

# ilk olarak, anahtar kelimeleri bir txt dosyasından okuyup bir liste olarak depolayalım:
with open('keywords.txt', 'r') as f:
    keywords = f.read().splitlines()

# Daha sonra, iş ilanını başka bir txt dosyasından okuyalım:
with open('job.txt', 'r') as f:
    job_description = f.read()

# Ardından, kullanıcıdan seçilecek CV dosyasını açalım:
import PyPDF2

with open('cv.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    cv_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        cv_text += page.extract_text()


# Daha sonra, anahtar kelimeleri ve iş ilanı metnini temizleyelim:
import re

# Anahtar kelimeleri küçük harfe çevirin ve gereksiz boşlukları kaldırın
keywords = [re.sub(r'\s+', ' ', keyword.strip().lower()) for keyword in keywords]
# İş ilanı metnini gereksiz boşlukları kaldırarak temizleyin
job_description = re.sub(r'\s+', ' ', job_description.strip().lower())
# CV metnini gereksiz boşlukları kaldırarak temizleyin
cv_text = re.sub(r'\s+', ' ', cv_text.strip().lower())


# anahtar kelimeleri ve iş ilanı metnini karşılaştırarak benzerlik oranını hesaplayalım ve sonucu ekrana yazdıralım:
import difflib

# Anahtar kelimelerle iş ilanı metni arasındaki benzerlik oranını hesaplayın
match_ratio = difflib.SequenceMatcher(None, ' '.join(keywords), job_description).ratio()

# Seçilen CV'deki anahtar kelimelerle iş ilanı arasındaki benzerlik oranını hesaplayın
match_ratio_cv = difflib.SequenceMatcher(None, ' '.join(keywords), cv_text).ratio()

# Sonucu ekrana yazdırın
print(f"Iş ilanı metni ile anahtar kelimeler arasındaki benzerlik oranı: {match_ratio:.2%}")
print(f"Seçilen CV ile anahtar kelimeler arasındaki benzerlik oranı: {match_ratio_cv:.2%}")
