class Player:
    def is_valid(self):
        return self.name != "" and self.floor != "" and self.room_number != ""

    def separate_args_with_commas(self, *args):
        args = map(lambda x: str(x), args)
        return ",".join(args)

    def to_csv_row(self):
        return self.separate_args_with_commas(self.name, self.tele_handle, self.floor, self.room_number, self.faculty,
                                              self.gender_pref, self.gender, self.prank_tol, self.likes, self.dislikes)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name').replace(",", ";")
        self.tele_handle = kwargs.get('tele_handle').replace(",", ";")
        try:
            self.floor = int(kwargs.get('floor'))
        except ValueError:
            self.floor = 0
        self.room_number = kwargs.get('room_number').replace(",", ";")
        self.faculty = kwargs.get('faculty').replace(",", ";")
        self.gender_pref = kwargs.get('gender_pref').replace(",", ";")
        self.gender = kwargs.get('gender').replace(",", ";")
        self.prank_tol = kwargs.get('prank_tol').replace(",", ";")
        self.likes = kwargs.get('likes').replace(",", ";")
        self.dislikes = kwargs.get('dislikes').replace(",", ";")

    def __repr__(self):
        return str(self.name)
