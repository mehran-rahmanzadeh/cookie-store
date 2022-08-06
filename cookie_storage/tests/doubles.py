class SessionDouble(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modified = False

    def flush(self):
        self.clear()
        self.modified = True


class RequestDouble:
    def __init__(self, session: SessionDouble, *args, **kwargs):
        self.session = session


class DataDouble:
    def __init__(self, data, *args, **kwargs):
        self.data = data
