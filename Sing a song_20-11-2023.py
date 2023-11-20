class Song():
    lyrics=[]
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing(self):
        for i in lyrics:
            print(i)

lyric=["Happy Birthday","To youuu","May god","Bless You"]
s1=Song(lyric)
s1.sing()    
