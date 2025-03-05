import os

folder_path = r"C:\Users\Dell\Desktop\Comini\Bollywood\Songs_Dataset_new\New romantic" 

def load_songs(folder_path):
    songs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                songs.append(file.read().strip())  # Read and strip extra spaces
    return songs

songs = load_songs(folder_path)

with open("bollywood_songs_dataset.txt", "w", encoding="utf-8") as f:
    f.write("\n\n===NEW SONG===\n\n".join(songs))

print(f"Loaded {len(songs)} songs into dataset! Saved as 'bollywood_songs_dataset.txt'.")
