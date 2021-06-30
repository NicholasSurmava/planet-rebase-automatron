class Forager:
    def __init__(self, source, site_type) -> None:
        self.source = source

    def hello(self):
        return f'Hello {self.source}'
