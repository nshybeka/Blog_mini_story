class Post:
    def __int__(self):
        self.id = None
        self.title = None
        self.subtitle = None
        self.body = None

    def set_data(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body


