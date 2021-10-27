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

mycursor.execute("SELECT * FROM game")


sql = """
    INSERT INTO game (id, name, category, brand, year_released, price) 
    VALUES (%s, %s, %s, %s, %s, %s)
"""


sql = """
    UPDATE game 
    SET name = %s, category = %s, brand = %s, year_released = %s, price = %s
    WHERE id = %s
"""


sql = "DELETE FROM game WHERE id = %s"


sql = "SELECT * FROM game WHERE id = %s"


sql = "SELECT * FROM game WHERE name LIKE %s"



# Week 4: API for mobile app


