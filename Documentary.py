   
import Media

class Documentary(Media.Media):
    def __init__(self, i, n, di, Is, u, du, c, t):
        super().__init__(i, n, di, Is, u, du, c)
        self.truth = t

    def show_info(self):
        return super().show_info() , 'a truth taken from: %s' %self.truth