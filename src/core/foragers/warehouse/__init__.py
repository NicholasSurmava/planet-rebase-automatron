from .. import Forager


model = {
    'tower_id': 12345
}


class Site_Forager(Forager):
    def get_towers(self):
        return model
