#!/usr/bin/env python3

from khub import app
import os

if __name__ == "__main__":
    if os.environ.get('FLASK_DEBUG', 'N').upper()[0] == "Y":
        app.run(host='0.0.0.0', port=8080, debug=True)
    else:         
        from waitress import serve
        serve(app, host='0.0.0.0', port=8080)