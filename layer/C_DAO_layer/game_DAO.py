# Package in pip
from typing import List

# Package of project owner
from app import database as db
from DTO.game_DTO import game


class game_DAO():    
    def read_games_DAO() -> List[game]:
        # games = game.query.all() -> ORM old

        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM game")
        myresult = mycursor.fetchall()

        game_list = list()
        for g in myresult:
            game_test = game(g[0], g[1], g[2], g[3], g[4], g[5])    
            game_list.append(game_test)

        return game_list 
    
    def create_game_DAO(game_created: game) -> bool:
        game_result = False

        # Check all type of data have inputed
        if game_DAO_subclass.check_type_game_created(game_created):
            # db.session.add(game_created)
            # db.session.commit()
            
            mycursor = db.cursor()
            sql = """
                INSERT INTO game (id, name, category, brand, year_released, price) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
            val = (
                game_created.id,
                game_created.name, 
                game_created.category,
                game_created.brand,
                game_created.year_released,
                game_created.price
            )
            mycursor.execute(sql, val)

            db.commit()
            game_result = True
        else:
            pass    # That's mean game_result still equal False
        return game_result

    def update_game_DAO(game_edited: game) -> bool:
        game_result = False
     
        if game_DAO_subclass.check_type_game_created(game_edited):
            # game_details = game.query.get(game_edited.id)

            # game_details.id = game_edited.id
            # game_details.name = game_edited.name
            # game_details.category = game_edited.category
            # game_details.brand = game_edited.brand
            # game_details.year_released = game_edited.year_released
            # game_details.price = game_edited.price

            # db.session.commit()

            mycursor = db.cursor()
            sql = """
                UPDATE game 
                SET name = %s, category = %s, brand = %s, year_released = %s, price = %s
                WHERE id = %s"""
            val = (
                    game_edited.name,
                    game_edited.category,
                    game_edited.brand,
                    game_edited.year_released,
                    game_edited.price,
                    game_edited.id
                )

            mycursor.execute(sql, val)
            db.commit()

            game_result = True
        else:    # That's mean game_result still equal False
            pass
        return game_result
    
    def delete_game_DAO(game_id: int) -> bool:
        # game_deleted = game.query.get(game_id)
        
        # db.session.delete(game_deleted)
        # db.session.commit()

        mycursor = db.cursor()

        sql = "DELETE FROM game WHERE id = %s"
        adr = (game_id, )

        mycursor.execute(sql, adr)
        db.commit()

        return True

    def read_game_details_DAO(game_id: int) -> game:
        # game_result = game.query.get(game_id)

        mycursor = db.cursor()
        sql = "SELECT * FROM game WHERE id = %s"
        game_temp = (game_id, )
        mycursor.execute(sql, game_temp)

        myresult = mycursor.fetchone()

        game_result = game(
            myresult[0],
            myresult[1],
            myresult[2],
            myresult[3],
            myresult[4],
            myresult[5]
        )
                
        return game_result
    
    def search_games_DAO(keyword_searched: str) -> List[game]:
        # games = game.query.filter(game.name.like(keyword_searched)).all()
        mycursor = db.cursor()
        
        sql = "SELECT * FROM game WHERE name LIKE %s"
        val = (keyword_searched, )

        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()

        game_list = list()
        for g in myresult:
            game_test = game(g[0], g[1], g[2], g[3], g[4], g[5])    
            game_list.append(game_test)

        return game_list


class game_DAO_subclass():
    def check_type_game_created(game_created: game) -> bool:
        try:
            year_released_checking = int(game_created.year_released)
            price_checking = float(game_created.price)
            if (
                type(year_released_checking) == int
                and type(price_checking) == float
            ):
                return True
        except:
            return False
        