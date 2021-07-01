class Forager:
    def __init__(self, source, site_type) -> None:
        self.source = source

    def hello(self):
        return f'Hello {self.source}'

    def __connect_to_db(self):
        return 'connected to db'

    def __connect_to_api(self):
        return 'connected to api'
