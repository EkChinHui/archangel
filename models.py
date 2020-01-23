class Player:
        def is_valid(self):
                return self.name != "" and self.floor != "" and self.room_number != ""

        def separate_args_with_commas(self, *args):
            args = map(lambda x: str(x), args)
            return ",".join(args)

        def to_csv_row(self):
            return self.separate_args_with_commas(self.name, self.fbname, self.floor, self.room_number, self.contact_number, self.gender, self.year, self.gender_pref, self.faculty, self.interests)

        def __init__(self, **kwargs):
                self.name = kwargs.get('name').replace(",", ";")
                self.fbname = kwargs.get('fbname').replace(",", ";")
                try:
                        self.floor = int(kwargs.get('floor'))
                except ValueError:
                        self.floor = 0
                self.room_number = kwargs.get('room_number').replace(",", ";")
                self.contact_number = kwargs.get('contact_number').replace(",", ";")
                self.gender = kwargs.get('gender').replace(",", ";")
                self.year = kwargs.get('year').replace(",", ";")
                self.gender_pref = kwargs.get('gender_pref').replace(",", ";")
                self.faculty = kwargs.get('faculty').replace(",", ";")
                self.interests = kwargs.get('interests').replace(",", ";")                
                
        def __repr__(self):
                return str(self.name)

