# 5-1 用魔术方法让自定义类像 list 一样工作

class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, idx):
        return self.songs[idx]

    #def __repr__(self):
    #    return f"Playlist({len(self)} songs)"

p = Playlist(["a", "b", "c"])
print(len(p), p[0], p[-1], p[1:])
print(p)