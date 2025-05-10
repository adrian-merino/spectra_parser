from brukeropusreader import read_file

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/parse_spectra", methods=["POST"])
def parse_spectra():
    try:
        data = request.get_json()

        if not data or "input" not in data:
            return "Error: No input received"

        spectra_list = read_file(data["input"])

        wavenum = [float(x) for x in list(spectra_list.get_range("AB"))]
        abs = [float(x) for x in list(spectra_list["AB"][0:len(wavenum)])]
        
        return jsonify({
            "absorbances": str(abs),
            "wavenumbers": str(wavenum),
            "input_received": data["input"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)

