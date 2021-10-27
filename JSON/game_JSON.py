import app

ma = app.marshmallow

# For converting data of SQL type to JSON
class game_JSON(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'brand', 'year_released', 'price')

game_schema = game_JSON()               # With single json result
games_schema = game_JSON(many=True)     # With many json result (list of json)