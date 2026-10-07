from flask import Flask

app = Flask(__name__)

@app.route('/parque/')
def inicio():
    return """
    <html>
    <body style="font-family: Arial; text-align: center; background: #fff8e1; padding: 30px;">
        <h1 style="color: #e65100; font-size: 40px;">🎡 Bem-vindo ao Parque de Diversões! 🎢</h1>
        <p style="font-size: 22px; color: #444;">Escolha um brinquedo e divirta-se!</p>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 25px; margin-top: 30px;">
        
            <a href="/parque/carrinhobatebate/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://i.ytimg.com/vi/nw2Id4AINCk/maxresdefault.jpg" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #d81b60;">🚗 Carrinho Bate-Bate</h3>
                </div>
            </a>

            <a href="/parque/rodagigante/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR2sW20udoPn5NH_DUM41e-Z6nHpbx9nR9XMUI8Epdsg&s" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #ff8f00;">🎡 Roda Gigante</h3>
                </div>
            </a>

            <a href="/parque/montanharussa/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://conteudo.imguol.com.br/c/entretenimento/a8/2021/08/13/montanha--russa-1628865040239_v2_1440x1920.jpg" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #e53935;">🏔️ Montanha-Russa</h3>
                </div>
            </a>

            <a href="/parque/carrossel/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://www.hotzone.com.br/sites/default/files/styles/1024x768/public/carrossel-001.jpg?itok=kMh9K6lP" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #7b1fa2;">🎠 Carrossel</h3>
                </div>
            </a>

            <a href="/parque/barcodivertido/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://sc04.alicdn.com/kf/Hf884b2ec30f34fd486dbad52535a4cd7M.jpg" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #0288d1;">🚤 Barco Divertido</h3>
                </div>
            </a>

            <a href="/parque/casasustos/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://images.unsplash.com/photo-1509248961825-943c46bfd09b?w=150&h=150&fit=crop" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #37474f;">👻 Casa dos Sustos</h3>
                </div>
            </a>

            <a href="/parque/torrequeda/" style="text-decoration: none;">
                <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px #0002; width: 200px;">
                    <img src="https://images.unsplash.com/photo-1518790730533-5b2855c9e2d5?w=150&h=150&fit=crop" 
                         style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
                    <h3 style="color: #455a64;">⬇️ Torre de Queda</h3>
                </div>
            </a>
        </div>
    </body>
    </html>
    """

@app.route('/parque/carrinhobatebate/')
def carrinho_bate_bate():
    return """
    <body style="font-family: Arial; text-align: center; background: #fff3e0; padding: 50px;">
        <h1 style="font-size: 35px;">🚗 Carrinho Bate-Bate! 💥</h1>
        <p style="font-size: 22px;">Divirta-se batendo sem medo!</p>
        <a href="/parque/" style="font-size: 18px; color: #e65100;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/rodagigante/')
def roda_gigante():
    return """
    <body style="font-family: Arial; text-align: center; background: #fff8e1; padding: 50px;">
        <h1 style="font-size: 35px;">🎡 Roda Gigante! 😍</h1>
        <p style="font-size: 22px;">Que vista linda lá de cima!</p>
        <a href="/parque/" style="font-size: 18px; color: #ff8f00;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/montanharussa/')
def montanha_russa():
    return """
    <body style="font-family: Arial; text-align: center; background: #ffebee; padding: 50px;">
        <h1 style="font-size: 35px;">🏔️ Montanha-Russa! 🎢</h1>
        <p style="font-size: 22px;">Segura firme que vem muita emoção!</p>
        <a href="/parque/" style="font-size: 18px; color: #e53935;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/carrossel/')
def carrossel():
    return """
    <body style="font-family: Arial; text-align: center; background: #f3e5f5; padding: 50px;">
        <h1 style="font-size: 35px;">🎠 Carrossel! 🐴</h1>
        <p style="font-size: 22px;">Que experiência doce e tranquila!</p>
        <a href="/parque/" style="font-size: 18px; color: #7b1fa2;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/barcodivertido/')
def barco_divertido():
    return """
    <body style="font-family: Arial; text-align: center; background: #e1f5fe; padding: 50px;">
        <h1 style="font-size: 35px;">🚤 Barco Divertido! 🌊</h1>
        <p style="font-size: 22px;">Água, alegria e muita diversão!</p>
        <a href="/parque/" style="font-size: 18px; color: #0288d1;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/casasustos/')
def casa_sustos():
    return """
    <body style="font-family: Arial; text-align: center; background: #eceff1; padding: 50px;">
        <h1 style="font-size: 35px;">👻 Casa dos Sustos! 😱</h1>
        <p style="font-size: 22px;">Será que teve coragem de chegar até o fim?</p>
        <a href="/parque/" style="font-size: 18px; color: #37474f;">← Voltar ao parque</a>
    </body>
    """

@app.route('/parque/torrequeda/')
def torre_queda():
    return """
    <body style="font-family: Arial; text-align: center; background: #f5f5f5; padding: 50px;">
        <h1 style="font-size: 35px;">⬇️ Torre de Queda! 😵💫</h1>
        <p style="font-size: 22px;">Prepara o coração... e cai!</p>
        <a href="/parque/" style="font-size: 18px; color: #455a64;">← Voltar ao parque</a>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)