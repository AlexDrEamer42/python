class Track:

    def __init__(self,name,length):
        self.name = name
        self.length = length

    def __str__(self):
        return(f'{self.name} - {self.length}')

    def __gt__(self,other):
        return self.length > other.length
    
    def __eq__(self,other):
        return self.length == other.length

class Album:

    def __init__(self,name,group,tracks):
        self.name = name
        self.group = group
        self.tracks = []
        for song in tracks:
            track = Track(song[0],song[1])
            self.tracks.append(track)
        
    def __str__(self):
        print(f'Name group: {self.group}')
        print(f'Name album: {self.name}')
        print('Tracks:')
        for track in self.tracks:
            print('       ',track)
        return('')

    def add_track(self,track):
        self.tracks.append(track)
    
    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.length
        return(duration)

album1 = Album('Коллекционер оружия','Сплин',[['Будь моей тенью',5],['Чёрный цвет солнца',8],['Любовь идёт по проводам',4]])
print(album1)
print('----------------')
print(f'Длительность звучания: {album1.get_duration()}')
print()
album2 = Album('Americana','The Offspring',[['Have You Ever',4],['Staring at the Sun',2],['Pretty Fly',3]])
print(album2)
print('----------------')
print(f'Длительность звучания: {album2.get_duration()}')
print()
print (album1.tracks[0] > album1.tracks[1])
print (album1.tracks[0] < album2.tracks[0])
print (album1.tracks[2] == album2.tracks[0])