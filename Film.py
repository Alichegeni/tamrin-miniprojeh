import Media

class Film(Media.Media):
    def __init__(self, i, n, di, Is, u, du, c, ci):
        super().__init__(i, n, di, Is, u, du, c)
        self.cinema = ci
    
    def show_info(self):
        return super().show_info() , 'Cinema: %s' %self.cinema