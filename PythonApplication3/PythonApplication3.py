from flask import Flask, render_template_string

app = Flask(__name__)

html_content = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Flask</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label, input, button {
            display: block;
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form method="POST">
        <label for="nama">Nama:</label>
        <input type="text" id="nama" name="nama">
        <button type="submit">Kirim</button>
    </form>

    {% if nama %}
        <p>Halo, {{ nama }}!</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Mengambil data dari form
        nama = request.form.get('nama')
        return render_template_string(html_content, nama=nama)
    return render_template_string(html_content, nama=None)

if __name__ == '__main__':
    app.run(debug=True)
