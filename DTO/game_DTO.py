import app

# db = app.database

# # DTO use with ORM
# class game(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False, unique=True)
#     category = db.Column(db.String(20), nullable=False)
#     brand = db.Column(db.String(20), nullable=False)
#     year_released = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Float, nullable=False)

#     def __init__(self, id, name, category, brand, year_released, price):
#         self.id = id
#         self.name = name
#         self.category = category
#         self.brand = brand
#         self.year_released = year_released
#         self.price = price

#     def __repr__(self):
#         return '<Name %r>' % self.name


# DTO use with primary SQL
db = app.database

class game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    year_released = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


    def __init__(self, id, name, category, brand, year_released, price):
        self.id = id
        self.name = name
        self.category = category
        self.brand = brand
        self.year_released = year_released
        self.price = price

    def __repr__(self):
        return '<Name %r>' % self.name



