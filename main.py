from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Nama : Hana Angelyn Budijono</p><p>Tempat,Tanggal lahir : Malang, 1 Agustus 2004</p><p>Alamat : Perumahan banjar arum asri singosari, Malang </p><p> Jenis kelamin : Perempuan </p><p> Agama : Kristen </p><p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
