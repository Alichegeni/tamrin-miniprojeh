import Media

class Clip(Media.Media):
    def __init__(self, i, n, di, Is, u, du, c, s):
        super().__init__(i, n, di, Is, u, du, c)
        self.shortened = s

    def show_info(self):
        return super().show_info() , 'shortened from: %s' %self.shortened