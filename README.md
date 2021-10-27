# Week 2: N-layer 

### 1. Architecture

![alt text](https://raw.githubusercontent.com/huanNguyen97/drawio-github/master/3-layer.drawio.png)

### 2. File structure

![alt text](https://raw.githubusercontent.com/huanNguyen97/drawio-github/master/File%20structure.drawio.png)

### 3. Issues exist

- Http method 'PUT' and 'DELETE' cannot use for update_game() and delete_game(). Have used 'POST' for insteading and it's work.
- Some code in DAO layer violate DRY. Fix later

# Week 3: SQL Primary or ORM
SQL primary -> ORM

mycursor.execute("SELECT * FROM game")  ->  games = game.query.all()  


sql = """
    INSERT INTO game (id, name, category, brand, year_released, price) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""
-> 
db.session.add(game_created)
db.session.commit()


sql = """
    UPDATE game 
    SET name = %s, category = %s, brand = %s, year_released = %s, price = %s
    WHERE id = %s
"""
->
game_details = game.query.get(game_edited.id)

game_details.id = game_edited.id
game_details.name = game_edited.name
game_details.category = game_edited.category
game_details.brand = game_edited.brand
game_details.year_released = game_edited.year_released
game_details.price = game_edited.price

db.session.commit()


sql = "DELETE FROM game WHERE id = %s"
->
game_deleted = game.query.get(game_id)
        
db.session.delete(game_deleted)
db.session.commit()


sql = "SELECT * FROM game WHERE id = %s"    ->  game_result = game.query.get(game_id)


sql = "SELECT * FROM game WHERE name LIKE %s"   ->  games = game.query.filter(game.name.like(keyword_searched)).all()



# Week 4: API for mobile app
From 6 API at first (render Jinja2Template), create more 6 api just response json data for react native fetching to. Total 12 API

@app.route('/api/get_all', methods=['GET']),
@app.route('/api/create-game', methods=['POST']),
@app.route('/api/update-game/<int:game_id>', methods=['PUT']),
@app.route('/api/delete-game/<int:game_id>', methods=['DELETE']),
@app.route('/api/search-games', methods=['GET', 'POST']),
@app.route('/api/read-game-details/<int:game_id>', methods=['GET'])


