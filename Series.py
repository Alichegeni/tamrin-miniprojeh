   
import Media

class Series(Media.Media):
    def __init__(self, i, n, di, Is, u, du, c, s, se):
        super().__init__(i, n, di, Is, u, du, c)
        self.section = s
        self.season = se

    def show_info(self):
        return super().show_info() , 'section: %i , season: %i' %(self.section , self.season)