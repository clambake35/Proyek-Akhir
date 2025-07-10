from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        tanggal = request.form['tanggal']
        no_hp = request.form['no_hp']
        # You can process/store this data as needed
        return f"<h2>Terima kasih, {nama}! Data Anda telah terkirim.</h2>"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
