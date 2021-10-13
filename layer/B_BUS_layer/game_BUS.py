# Package in pip
from typing import List

# Package of project owner
from layer.C_DAO_layer.game_DAO import game_DAO
from DTO.game_DTO import game


class game_BUS():
    def read_games_BUS() -> List[game]:
        games = game_DAO.read_games_DAO()
        return games
    
    def create_game_BUS(game_created: game) -> bool:
        game_result = game_DAO.create_game_DAO(game_created) 
        return game_result   

    def update_game_BUS(game_edited: game) -> bool:
        game_result = game_DAO.update_game_DAO(game_edited)    
        return game_result
    
    def delete_game_BUS(game_id: int) -> bool:
        game_result = game_DAO.delete_game_DAO(game_id)
        return game_result

    def read_game_details_BUS(game_id: int) -> game:
        game_result = game_DAO.read_game_details_DAO(game_id)
        return game_result
    
    def search_games_BUS(keyword_searched: str) -> List[game]:
        games_list = game_DAO.search_games_DAO(keyword_searched)
        return games_list