import Actor
import pytube

class Media:
    def __init__(self, i, n, di, Is, u, du, c):
        self.id = i
        self.name = n
        self.director = di
        self.IMDB_Score = Is
        self.url = u
        self.duration = du
        self.casts = c

    def show_info(self):
        actors = self.casts
        casts = Actor.Actor(actors)
        return 'id: %s , name: %s , director: %s , IMDB Score: %f , url: %s , duration: %i , casts: %s'%(self.id , 
        self.name , self.director , self.IMDB_Score , self.url , self.duration , casts.shows()) 
    
    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./' , filename='test.mp4')