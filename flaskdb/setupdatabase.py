from index import Puppy, db

db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Franky', 3)

db.session.add_all([sam, frank])
db.session.commit()