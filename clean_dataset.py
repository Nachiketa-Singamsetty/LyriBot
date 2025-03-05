import re

with open("bollywood_songs_dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

cleaned_text = re.sub(r"[^\u0900-\u097F,।!? \n=]", "", text) 

cleaned_text = re.sub(r"\n+", "\n", cleaned_text)  
cleaned_text = re.sub(r" +", " ", cleaned_text)  

with open("cleaned_songs_dataset.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Cleaning complete!. Saved as 'cleaned_songs_dataset.txt'.")
