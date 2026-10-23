from flask import Flask, render_template, request, jsonify
from algorithms import ALGORITHMS
from time import process_time
from statistics import median

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


# This function is written with help from Claude
def algo(algorithm, numbers):
    times = []
    for _ in range(3):
        copied = numbers.copy()

        start_time = process_time()
        intermediate = algorithm(copied)
        end_time = process_time()

        output = intermediate if intermediate is not None else copied

        times.append(end_time - start_time)

    return output, median(times)


@app.route("/")
def index():
    return render_template("index.html")


# This function is written with help from Claude
@app.route("/api/benchmark", methods=["POST"])
def benchmark():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON."}), 400

    if not data.get("numbers"):
        return jsonify({"error": "Enter at least one number."}), 400

    if not data.get("algorithm"):
        return jsonify({"error": "Please select an algorithm."}), 400

    algorithm = data["algorithm"]
    if algorithm not in ALGORITHMS:
        return jsonify({"error": "Invalid algorithm."}), 400

    if not isinstance(data["numbers"], list):
        return jsonify({"error": "Enter at least one number."}), 400

    if len(data["numbers"]) > 100000:
        return jsonify({"error": "Maximum 100,000 numbers."}), 400

    for x in data["numbers"]:
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            return jsonify({"error": "Please enter numbers only."}), 400

    sorted_list, median_time = algo(ALGORITHMS[algorithm], data["numbers"])

    return jsonify({"name": algorithm, "sorted": sorted_list, "time": median_time})


if __name__ == "__main__":
    app.run(debug=True)
