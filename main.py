# Package in pip
from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash
)

# Package of project owner
import app
from DTO.game_DTO import game
from layer.B_BUS_layer.game_BUS import game_BUS


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


# Read details
@app.route('/read-game-details/<int:game_id>', methods=['GET'])
async def read_game_details(game_id):
    game_details = game_BUS.read_game_details_BUS(game_id)
    return render_template('game/read_game_details.html', game=game_details)


# Search by name
@app.route('/search-games', methods=['GET', 'POST'])
async def search_games():
    keyword = request.form['text-of-searching']
    keyword_searched = "%{0}%".format(keyword)
    games_list = game_BUS.search_games_BUS(keyword_searched)
    return render_template('game/read_games.html', games_list=games_list)
# ---------------------------------------------------
# ---------------------------------------------------
# End app


if __name__ == '__main__':
    app.run(
        debug=True
    )