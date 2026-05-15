import uuid
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Configurando a pasta onde as imagens serão salvas
UPLOAD_FOLDER = 'static/assets'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ===========================================================================

@app.route("/")
def index():
    return render_template("index.html")

# ===========================================================================

# Cadastro de plataformas
@app.route("/cadastro_plataformas", methods=['GET', 'POST'])
def cadastro_plataformas():
    if request.method == 'POST':
        cod_plataforma = str(uuid.uuid4())  # Gera o UUID como identificador único
        nome = request.form["nome"]
        fabricante = request.form["fabricante"]

        imagem = request.files['imagem']

        if imagem:
            extensao = imagem.filename.split('.')[-1]  # Obtém a extensão do arquivo
            nome_imagem = f"{nome.strip().lower().replace(" ", "_")}.{extensao}"  # Nome da imagem baseado no nome da plataforma
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], nome_imagem)

            # Salva a imagem na pasta de uploads
            imagem.save(caminho_imagem)

        with open('models/plataformas.txt', 'a') as arquivo:
            arquivo.write(f"{cod_plataforma};{nome};{fabricante};{caminho_imagem}\n")
        
        return redirect("/consulta_plataformas")
    
    return render_template("cadastro_plataformas.html")

# ===========================================================================

# Consulta de plataformas
@app.route("/consulta_plataformas")
def consulta_plataformas():
    plataformas = []
    numero_linha = 0  # Variável separada para contar o número da linha
    with open('models/plataformas.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            plataformas.append({
                'linha': numero_linha,  # Use numero_linha aqui
                'cod_plataforma': dados[0],
                'nome': dados[1],
                'fabricante': dados[2],
                'imagem': dados[3]
            })
            numero_linha += 1  # Incrementa o número da linha corretamente
    
    return render_template("consulta_plataformas.html", plataformas=plataformas)


# ===========================================================================


# Função de excluir plataforma
@app.route("/excluir_plataforma", methods=['GET', 'POST'])
def excluir_plataforma():
    linha_para_excluir = int(request.args.get('linha'))
    caminho_arquivo = 'models/plataformas.txt'
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Obtém a linha a ser excluída
    linha_excluida = linhas[linha_para_excluir]
    
    # Extrai o caminho da imagem da linha (assumindo que está na 4ª posição)
    dados = linha_excluida.strip().split(';')
    caminho_imagem = dados[3]  # O caminho da imagem está na quarta posição
    
    # Exclui a imagem se existir
    if os.path.exists(caminho_imagem):
        os.remove(caminho_imagem)
    
    # Remove a linha do arquivo
    del linhas[linha_para_excluir]
    
    # Grava o arquivo atualizado sem a linha removida
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return redirect("/consulta_plataformas")



# ===========================================================================
# ===========================================================================
# ===========================================================================

# Cadastro de jogos
@app.route("/cadastro_jogos", methods=['GET', 'POST'])
def cadastro_jogos():
    if request.method == 'POST':
        cod_jogo = str(uuid.uuid4())  # Gera o UUID como identificador único
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        lancamento = request.form["lancamento"]
        cod_plataforma = request.form["plataforma"]
        
        # Grava o jogo no arquivo de texto
        with open('models/jogos.txt', 'a') as arquivo:
            arquivo.write(f"{cod_jogo};{titulo};{genero};{lancamento};{cod_plataforma}\n")
        
        return redirect("/consulta_jogos")
    
    # Lê as plataformas do arquivo plataformas.txt para preencher o select
    plataformas = []
    with open('models/plataformas.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            plataformas.append({
                'cod_plataforma': dados[0],
                'nome': dados[1],
                'fabricante': dados[2]  # Inclui o campo 'fabricante' conforme o formato dos dados
            })

    
    return render_template("cadastro_jogos.html", plataformas=plataformas)

# ===========================================================================

# Consulta de jogos
@app.route("/consulta_jogos")
def consulta_jogos():
    jogos = []
    numero_linha = 0
    with open('models/jogos.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            jogos.append({
                'linha': numero_linha,
                'cod_jogo': dados[0],
                'titulo': dados[1],
                'genero': dados[2],
                'lancamento': dados[3],
                'cod_plataforma': dados[4]
            })
            numero_linha += 1
    return render_template("consulta_jogos.html", jogos=jogos)

# ===========================================================================

# Corrigir a função de exclusão de jogos
@app.route("/excluir_jogo", methods=['GET', 'POST'])
def excluir_jogo():
    linha_para_excluir = int(request.args.get('linha')) 
    caminho_arquivo = 'models/jogos.txt'
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    del linhas[linha_para_excluir]  

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return redirect("/consulta_jogos")


# ===========================================

# Editar plataforma
@app.route("/editar_plataforma", methods=['GET', 'POST'])
def editar_plataforma():
    caminho_arquivo = 'models/plataformas.txt'

    if request.method == 'POST':
        # Capturando a linha através de um campo GET (query string)
        linha = request.args.get("linha")  # Pega a linha passada via GET
        
        linha = int(linha)
        nome = request.form["nome"]
        fabricante = request.form["fabricante"]

        # Lendo as linhas do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Atualizando a linha com os novos dados, sem modificar o UUID ou a imagem
        dados = linhas[linha].strip().split(';')
        cod_plataforma = dados[0]  # Mantém o UUID
        caminho_imagem = dados[3]  # Mantém o caminho da imagem

        nova_linha = f"{cod_plataforma};{nome};{fabricante};{caminho_imagem}\n"
        linhas[linha] = nova_linha

        # Reescrevendo o arquivo com os dados atualizados
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.writelines(linhas)

        return redirect("/consulta_plataformas")

    # Caso seja uma requisição GET, carregamos os dados da plataforma para edição
    linha = int(request.args.get('linha'))
    
    with open(caminho_arquivo, 'r') as arquivo:
        linha_plataforma = arquivo.readlines()[linha]

    dados = linha_plataforma.strip().split(';')
    plataforma = {
        'cod_plataforma': dados[0],
        'nome': dados[1],
        'fabricante': dados[2],
        'imagem': dados[3]
    }

    return render_template("editar_plataforma.html", plataforma=plataforma)



# Editar jogo
@app.route("/editar_jogo", methods=['GET', 'POST'])
def editar_jogo():
    caminho_arquivo = 'models/jogos.txt'
    
    if request.method == 'POST':
        # Capturando a linha através de um campo GET (query string)
        linha = int(request.args.get("linha"))  # Pega a linha passada via GET
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        lancamento = request.form["lancamento"]
        cod_plataforma = request.form["plataforma"]

        # Lendo as linhas do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Atualizando a linha com os novos dados, sem modificar o UUID
        dados = linhas[linha].strip().split(';')
        cod_jogo = dados[0]  # Mantém o UUID do jogo
        
        nova_linha = f"{cod_jogo};{titulo};{genero};{lancamento};{cod_plataforma}\n"
        linhas[linha] = nova_linha

        # Reescrevendo o arquivo com os dados atualizados
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.writelines(linhas)

        return redirect("/consulta_jogos")

    # Caso seja uma requisição GET, carregamos os dados do jogo para edição
    linha = int(request.args.get('linha'))  # Recupera a linha da query string
    with open(caminho_arquivo, 'r') as arquivo:
        linha_jogo = arquivo.readlines()[linha]

    dados = linha_jogo.strip().split(';')
    jogo = {
        'cod_jogo': dados[0],
        'titulo': dados[1],
        'genero': dados[2],
        'lancamento': dados[3],
        'cod_plataforma': dados[4]
    }

    # Lendo as plataformas para preencher o select
    plataformas = []
    with open('models/plataformas.txt', 'r') as arquivo:
        for linha_plataforma in arquivo:
            dados_plataforma = linha_plataforma.strip().split(';')
            plataformas.append({
                'cod_plataforma': dados_plataforma[0],
                'nome': dados_plataforma[1]
            })

    return render_template("editar_jogo.html", jogo=jogo, plataformas=plataformas)


# ===========================================

if __name__ == "__main__":
    app.run(debug=True)
