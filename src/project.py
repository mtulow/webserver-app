from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)

engine = create_engine("sqlite:///src/restaurant_menu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_restaurants():
    restaurants = session.query(Restaurant).all()
    for restaurant in restaurants:
        yield restaurant

def get_menu_items(restaurant_id: int):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    for item in items:
        yield item



@app.route('/')
@app.route('/restaurants/')
def index():
    output = get_restaurants()
    return render_template('index.html', restaurants=output)




# @app.route('/restaurants/<int:restaurant_id>/')
# def restaurant_menu(restaurant_id):
#     r = session.query(Restaurant).filter_by(id=restaurant_id)
#     items = get_menu_items(restaurant_id)
#     output = ''
#     output += '<h1><center>{}</center></h1>'.format(r.name)
#     for i in items:
#         output += i.name
#         output += '</br>'
#         output += i.price
#         output += '</br>'
#         output += i.description
#         output += '</br>'
#         output += '</br>'
#     return output



@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template('../templates/menu.html', restaurant=restaurant, items=items)



# Task 1: Create route for newMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"


# Task 2: Create route for editMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"


# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
