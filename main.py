# Package in pip
# Flask package
from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash,
    jsonify
)

# Package of project owner
import app
from DTO.game_DTO import game
from layer.B_BUS_layer.game_BUS import game_BUS

# JSON to response for react native
import JSON.game_JSON as JSON


app = app.application
app.config['SECRET_KEY'] = 'Huan and Mr.SonKK learn and teach SA together'

# Flask app
# ---------------------------------------------------
# ---------------------------------------------------
# CRUD
# Read all list
@app.route('/', methods=['GET'])
async def read_games():
    games_list = game_BUS.read_games_BUS()
    return render_template('game/read_games.html', games_list=games_list)


# Create new one
@app.route('/create-game', methods=['GET', 'POST'])
async def create_game():
    if request.method == 'POST':
        game_created = game(
            id = None,
            name = request.form['name'],
            category = request.form['category'],
            brand = request.form['brand'],
            year_released = request.form['year_released'],
            price = request.form['price']
        )

        game_result = game_BUS.create_game_BUS(game_created)

        if game_result:
            flash("You have created successfully", "create-success")
            return redirect(url_for('read_games'))
        else:
            flash("Your type of data was wrong", "create-fail")
            return redirect(url_for('create_game'))
    else:   # That's mean method is GET (read form of create a game)
        return render_template('game/create_game.html')


# Need to use HTTP method PUT in here, but it's not working
# POST for insteading is ok
# Temporary, ask Mr.Sonkk and fix later

# Violate DRY, fix later !!!
@app.route('/update-game/<int:game_id>', methods=['GET', 'POST'])
async def update_game(game_id):
    if request.method == 'POST':
        game_edited = game(
            id = request.form['id'],
            name = request.form['name'],
            category = request.form['category'],
            brand = request.form['brand'],
            year_released = request.form['year_released'],
            price = request.form['price']
        )

        game_result = game_BUS.update_game_BUS(game_edited)

        if game_result:
            flash('You have updated successfully', 'update-success')
            return redirect(url_for('read_games'))
        else:
            flash('Your type of data was wrong', 'update-fail')
            return redirect(url_for('update_game', game_id=game_edited.id))

    else:
        game_details = game_BUS.read_game_details_BUS(game_id)
        return render_template('game/update_game.html', game=game_details)


# Like update_game, this API need to use HTTP delete
# POST for insteading is ok
# Fix later
@app.route('/delete-game/<int:game_id>', methods=['GET', 'POST'])
async def delete_game(game_id):
    game_BUS.delete_game_BUS(game_id)
    flash('Game was deleted', 'delete-success')
    return redirect(url_for('read_games'))


# Search by name
@app.route('/search-games', methods=['GET', 'POST'])
async def search_games():
    keyword = request.form['text-of-searching']
    keyword_searched = "%{0}%".format(keyword)
    games_list = game_BUS.search_games_BUS(keyword_searched)
    return render_template('game/read_games.html', games_list=games_list)


# Read details
@app.route('/read-game-details/<int:game_id>', methods=['GET'])
async def read_game_details(game_id):
    game_details = game_BUS.read_game_details_BUS(game_id)
    return render_template('game/read_game_details.html', game=game_details)



# ---------------------------------------------------
# ---------------------------------------------------
# End app


# For React naitve fetching to... (Reactjs or react native)
# ---------------------------------------------------
# ---------------------------------------------------
# JSON read_all_games
@app.route('/api/get_all', methods=['GET'])
async def read_games_json():
    games_list = game_BUS.read_games_BUS()
    games_list_JSON = JSON.games_schema.dump(games_list)
    return jsonify(games_list_JSON)


# JSON create_game
@app.route('/api/create-game', methods=['POST'])
async def create_game_JSON():
    if request.method == 'POST':
        game_created = game(
            id = None,
            name = request.json['name'],
            category = request.json['category'],
            brand = request.json['brand'],
            year_released = request.json['year_released'],
            price = request.json['price']
        )

        game_result = game_BUS.create_game_BUS(game_created)
        
        if game_result:
            return JSON.game_schema.jsonify(game_created)
        else:
            pass
    else:   # That's mean method is GET (read form of create a game)
        pass


# JSON update_game
@app.route('/api/update-game/<int:game_id>', methods=['PUT'])
async def update_game_JSON(game_id):
    if request.method == 'PUT':
        game_edited = game(
            id = request.json['id'],
            name = request.json['name'],
            category = request.json['category'],
            brand = request.json['brand'],
            year_released = request.json['year_released'],
            price = request.json['price']
        )

        game_result = game_BUS.update_game_BUS(game_edited)

        if game_result:
            return JSON.game_schema.jsonify(game_edited)
        else:
            pass    # Don't really know need to do at here. Need some advice !!!

    else:
        pass    # Don't really know need to do at here. Need some advice !!!


# JSON delete_game
@app.route('/api/delete-game/<int:game_id>', methods=['DELETE'])
async def delete_game_JSON(game_id):
    game_BUS.delete_game_BUS(game_id)
    return jsonify({
        "title": "Deleted",
        "status": "Success"
    })


# JSON search_game
@app.route('/api/search-games', methods=['GET', 'POST'])
async def search_games_JSON():
    keyword = request.json['search_text']
    keyword_searched = "%{0}%".format(keyword)
    games_list = game_BUS.search_games_BUS(keyword_searched)
    games_list_JSON = JSON.games_schema.dump(games_list)
    return jsonify(games_list_JSON)


# JSON read_details_game
@app.route('/api/read-game-details/<int:game_id>', methods=['GET'])
async def read_game_details_JSON(game_id):
    game_details = game_BUS.read_game_details_BUS(game_id)
    games_details_JSON = JSON.game_schema.dump(game_details)
    return jsonify(games_details_JSON)


# ---------------------------------------------------
# ---------------------------------------------------
# End mobile

if __name__ == '__main__':
    app.run(
        # host="huan-sa-hsu-orm-react-native",
        port="8000",
        debug=True
    )