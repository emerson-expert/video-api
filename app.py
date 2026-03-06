from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/extract")
def extract():
    url = request.args.get("url")

    ydl_opts = {
        "quiet": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return jsonify({
        "title": info.get("title"),
        "thumbnail": info.get("thumbnail"),
        "video_url": info["url"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)