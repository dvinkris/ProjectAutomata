from flask import Flask, render_template, request

app = Flask(__name__)

def is_valid_string(s):
    steps = []
    def helper(subs):
        if subs == "":
            steps.append('"" → ε (diterima)')
            return True
        if len(subs) % 2 != 0:
            return False
        if subs[0] == '0' and subs[-1] == '0':
            steps.append(f'{subs} → cocok 0__0 → lanjut ke "{subs[1:-1]}"')
            return helper(subs[1:-1])
        elif subs[0] == '1' and subs[-1] == '1':
            steps.append(f'{subs} → cocok 1__1 → lanjut ke "{subs[1:-1]}"')
            return helper(subs[1:-1])
        elif subs[0] == '0' and subs[-1] == '1':
            steps.append(f'{subs} → cocok 0__1 → lanjut ke "{subs[1:-1]}"')
            return helper(subs[1:-1])
        elif subs[0] == '1' and subs[-1] == '0':
            steps.append(f'{subs} → cocok 1__0 → lanjut ke "{subs[1:-1]}"')
            return helper(subs[1:-1])
        return False

    valid = helper(s)
    return valid, steps

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    steps = []
    if request.method == "POST":
        input_str = request.form["binary_input"]
        valid, steps = is_valid_string(input_str)
        result = (input_str, valid)
    return render_template("index.html", result=result, steps=steps)

if __name__ == "__main__":
    app.run(debug=True)
