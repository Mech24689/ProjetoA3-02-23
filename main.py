from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajustar_parabola', methods=['GET', 'POST'])
def ajustar_parabola():
    if request.method == 'POST':
        coordenadas_x = [float(x) for x in request.form.getlist('coord-x')]
        coordenadas_y = [float(y) for y in request.form.getlist('coord-y')]

        if len(coordenadas_x) != 3 or len(coordenadas_y) != 3:
            return 'Por favor, forneça exatamente 3 coordenadas para x e y.'

        # Realiza o ajuste da parábola
        coefficients = np.polyfit(coordenadas_x, coordenadas_y, 2)
        a, b, c = coefficients

        xmin, xmax = min(coordenadas_x), max(coordenadas_x)
        area = area_parabola(lambda x: a * x ** 2 + b * x + c, xmin, xmax)

        return render_template('ajuste_parabola2.html', a=a, b=b, c=c, area=area)

    return render_template('ajuste_parabola2.html', a=None, b=None, c=None, area=None)

def area_parabola(f, xmin, xmax, n_points=1000):
    x_values = np.linspace(xmin, xmax, n_points)
    y_values = [f(x) for x in x_values]
    area = np.trapz(y_values, x_values)
    return area

if __name__ == '__main__':
    app.run(debug=True)
