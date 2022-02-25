from website import create_app ## Resumindo, o arquivo __init__.py se torna o construtor da pasta website

app = create_app()

if __name__ == '__main__': ## Isso obriga a execução do arquivo para rodar o servidor, não apenas a importação 
    app.run(debug=True) ## O parâmetro faz com que o servidor seja rerodado sempre que uma alteração seja feita no arquivo