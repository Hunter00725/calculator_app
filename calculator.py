from flask import Flask, render_template_string, request

app = Flask(__name__)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Cannot divide by zero.")
    return a / b


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Calculator Service</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .calc-card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; width: 320px; }
        h2 { color: #333; margin-bottom: 20px; }
        input, select { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; font-size: 16px; }
        button { width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; padding: 10px; background-color: #e2f0d9; border-radius: 5px; color: #385723; font-weight: bold; font-size: 18px; }
        .error { margin-top: 20px; padding: 10px; background-color: #fce4d6; border-radius: 5px; color: #c65911; font-weight: bold; }
    </style>
</head>
<body>
    <div class="calc-card">
        <h2>CI/CD Calculator App</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" placeholder="Enter first number" required value="{{ num1 }}">
            <select name="operation">
                <option value="add" {% if op == 'add' %}selected{% endif %}>+ Addition</option>
                <option value="sub" {% if op == 'sub' %}selected{% endif %}>- Subtraction</option>
                <option value="mul" {% if op == 'mul' %}selected{% endif %}>&times; Multiplication</option>
                <option value="div" {% if op == 'div' %}selected{% endif %}>&divide; Division</option>
            </select>
            <input type="number" step="any" name="num2" placeholder="Enter second number" required value="{{ num2 }}">
            <button type="submit">Calculate</button>
        </form>
        
        {% if result is not none %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    num1, num2, op = '', '', 'add'
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op = request.form['operation']
            
            if op == 'add': result = add(num1, num2)
            elif op == 'sub': result = subtract(num1, num2)
            elif op == 'mul': result = multiply(num1, num2)
            elif op == 'div': result = divide(num1, num2)
        except ValueError as e:
            error = str(e) if "divide" in str(e) else "Invalid numerical input."
            
    return render_template_string(HTML_TEMPLATE, result=result, error=error, num1=num1, num2=num2, op=op)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
