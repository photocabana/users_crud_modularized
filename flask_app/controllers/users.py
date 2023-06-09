from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports

# Create Users Controller

@app.route("/users/create", methods=['POST'])
def create_user():
    user_id = user.User.create_user(request.form)
    return redirect(f'/users/{user_id}/profile')


# Read Users Controller

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<int:id>/profile')
def profile(id):
    user1 = user.User.get_user_by_id(id)
    return render_template('profile.html', users = user1)

@app.route('/users/all')
def show_all_users():
    users_all = user.User.get_all_users()
    print(users_all[0].first_name)
    return render_template('home.html', users_all = users_all)


# Update Users Controller

@app.route('/users/<int:id>/update', methods=['POST', 'GET'])
def profile_edit_page(id):
    if request.method == 'GET':
        user1 = user.User.get_user_by_id(id)
        return render_template('edit_profile.html', users = user1)
    #if request.method == 'POST':
    user.User.update_user(request.form)
    return redirect('/users/all')

# Delete Users Controller

@app.route('/users/<int:id>/delete')
def delete_user_by_id(id):
    user.User.delete_user_by_id(id)
    return redirect('/users/all')


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.