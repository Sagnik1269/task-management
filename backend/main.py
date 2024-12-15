from website import create_app
from flask_cors import CORS

app = create_app()

# Configure CORS with specific settings
CORS(app, 
     supports_credentials=True, 
     origins=["http://localhost:5173"],  # Your frontend origin
     )

if __name__ == '__main__':
    app.run(debug=True)

    