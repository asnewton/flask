from index import Puppy, db

#CREATE
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

#READ
all_puppies = Puppy.query.all()
print(all_puppies)

#select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)
#filter
puppy_franky = Puppy.query.filter_by(name='Franky')
print(puppy_franky.all())


#UPDATE
puppy_first = Puppy.query.get(1)
puppy_first.age = 10
db.session.add(puppy_first)
db.session.commit()

#DELETE
puppy_second = Puppy.query.get(2)
db.session.delete(puppy_second)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
