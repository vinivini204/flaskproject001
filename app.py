from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui você pode adicionar o código para salvar os dados do usuário em seu banco de dados
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/library')
def library():
    books = ['João e Maria', 'Harry Porter e a pedra filosofal', 'Crime e vários castigo', 'A revolução dos bichos', 'A divina comédia', 'Romeu e Julieta']
    return render_template('library.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
