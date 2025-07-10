from flask import Flask, render_template, request, redirect, url_for
from models import db, User  # Import db dari models, lalu bind
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        tanggal = request.form['tanggal']
        no_hp = request.form['no_hp']

        tgl_baru = datetime.strptime(tanggal, '%Y-%m-%d').date()
        user = User(nama=nama, tanggal=tgl_baru, no_hp=no_hp)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('registrasi.html')


@app.route('/list')
def list():
    bulan = request.args.get('bulan', type=int)
    if bulan:
        users = User.query.filter(db.extract('month', User.tanggal) == bulan).all()
    else:
        users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list'))

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.nama = request.form['nama']
        user.tanggal = datetime.strptime(request.form['tanggal'], '%Y-%m-%d').date()
        user.no_hp = request.form['no_hp']
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('edit.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)