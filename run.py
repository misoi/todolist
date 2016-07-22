from app import app  
from flask import Flask

if __name__ == '__main':
	app.run(debug=True)


from app.main import views