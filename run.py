import os
path = "Z:\\Playlists"
dir_list = os.listdir(path)

for d in dir_list:
    file_list = os.listdir(os.path.join(path, d));
    playlist_pre = os.path.join(path,d,d+".m3u8");
    playlist_file = open(playlist_pre, "w", encoding='utf-8')
    mp3file_list = []
    for f in file_list:
        if f.endswith(".mp3"):
            mp3file_list.append (f + '\n')        
    playlist_file.writelines(mp3file_list)
    playlist_file.close()

print ("end of program")