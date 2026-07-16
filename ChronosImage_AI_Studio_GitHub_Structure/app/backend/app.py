from flask import Flask
app = Flask(__name__)

@app.get("/")
def health():
    return {"name": "ChronosImage AI Studio", "status": "ready"}

if __name__ == "__main__":
    app.run(port=8080)
