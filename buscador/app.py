from flask import Flask, request, render_template

# modulos proprios
from search_engine import SearchEngine

app = Flask(__name__)

print("Inicializando search engine")
se = SearchEngine()
print("Search engine inicializada")

@app.route('/', methods=['GET'])
def index():
    global se
    if 'termos' in request.args.keys():
        termos = request.args['termos']
        print("termo buscado eh: ",termos)
        results, busca = se.ranquear(termos)
        if busca == 0:
            return render_template('index.html', results=results, termos=termos)
        else:
            termos = busca
            print("termo buscado eh: ",busca)
            results, busca = se.ranquear(termos)
            return render_template('index.html', results=results, termos=termos)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


