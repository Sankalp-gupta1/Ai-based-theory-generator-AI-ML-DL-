<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Theory Generator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Theory Generator</h1>
        </header>
        <main>
            <h2>Generate a Theory</h2>
            <form action="/generate_theory" method="post">
                <label for="topic">Enter a Topic:</label>
                <input type="text" id="topic" name="topic" required>
                <button type="submit">Generate Theory</button>
            </form>
            {% if theory %}
                <div class="theory-box">
                    <h3>Generated Theory:</h3>
                    <p>{{ theory }}</p>
                </div>
            {% endif %}
        </main>
    </div>
</body>
</html>
