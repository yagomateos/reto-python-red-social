from flask import Flask, render_template, request, redirect, url_for, flash
from social_network import SocialNetwork

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para flash messages

# Crear una instancia de la red social
social_network = SocialNetwork()

# Crear algunos usuarios de ejemplo
social_network.create_user("usuario1", "Usuario Uno")
social_network.create_user("usuario2", "Usuario Dos")

# Crear algunos posts de ejemplo
social_network.create_post("usuario1", "¡Hola a todos! Este es mi primer post.")
social_network.create_post("usuario2", "¡Me encanta esta red social!")

@app.route('/')
def home():
  posts = social_network.posts
  users = social_network.users
  return render_template('home.html', posts=posts, users=users)

@app.route('/profile/<username>')
def profile(username):
  user = social_network.get_user(username)
  users = social_network.users
  if user:
      return render_template('profile.html', user=user, users=users)
  return "Usuario no encontrado", 404

@app.route('/post', methods=['POST'])
def create_post():
  content = request.form.get('content')
  username = request.form.get('username', 'usuario1')  # Usuario por defecto
  post = social_network.create_post(username, content)
  if post:
      flash('Post creado exitosamente!')
  else:
      flash('Error al crear el post')
  return redirect(url_for('home'))

@app.route('/follow/<username>', methods=['POST'])
def follow_user(username):
  current_user = social_network.get_user('usuario1')  # Usuario actual (por ahora hardcodeado)
  user_to_follow = social_network.get_user(username)
  if current_user and user_to_follow:
      current_user.follow(user_to_follow)
      flash(f'Ahora sigues a {username}!')
  return redirect(url_for('profile', username=username))

if __name__ == '__main__':
  app.run(debug=True)