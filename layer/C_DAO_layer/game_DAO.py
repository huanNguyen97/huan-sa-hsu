# Package in pip
from typing import List

# Package of project owner
from app import database as db
from DTO.game_DTO import game


class game_DAO():    
    def read_games_DAO() -> List[game]:
        games = game.query.all()    
        return games    
    
    def create_game_DAO(game_created: game) -> bool:
        game_result = False

        # Check all type of data have inputed
        if game_DAO_subclass.check_type_game_created(game_created):
            db.session.add(game_created)
            db.session.commit()
            game_result = True
        else:
            pass    # That's mean game_result still equal False
        return game_result

    def update_game_DAO(game_edited: game) -> bool:
        game_DAO_subclass.check(game_edited)
        game_result = False
     
        if game_DAO_subclass.check_type_game_created(game_edited):
            game_details = game.query.get(game_edited.id)

            game_details.id = game_edited.id
            game_details.name = game_edited.name
            game_details.category = game_edited.category
            game_details.brand = game_edited.brand
            game_details.year_released = game_edited.year_released
            game_details.price = game_edited.price

            db.session.commit()
            game_result = True
        else:    # That's mean game_result still equal False
            pass
        return game_result
    
    def delete_game_DAO(game_id: int) -> bool:
        game_deleted = game.query.get(game_id)
        
        db.session.delete(game_deleted)
        db.session.commit()

        return True

    def read_game_details_DAO(game_id: int) -> game:
        game_result = game.query.get(game_id)
        return game_result
    
    def search_games_DAO(keyword_searched: str) -> List[game]:
        games = game.query.filter(game.name.like(keyword_searched)).all()
        return games


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
    
    def check(game_edited: game):
        pass