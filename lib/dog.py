from model import Dog

def create_table(base, engine):
  """Creates the Dog table in the database."""
  base.metadata.create_all(engine)

def save(session, dog):
  """Saves a Dog object to the database."""
  session.add(dog)
  session.commit()

def get_all(session):
  """Retrieves all Dog objects from the database."""
  return session.query(Dog).all()

def find_by_name(session, name):
  """Retrieves a Dog object by its name."""
  return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
  """Retrieves a Dog object by its ID."""
  return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
  """Retrieves a Dog object by its name and breed."""
  return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
  """Updates the breed of a Dog object."""
  dog.breed = breed
  session.commit()

