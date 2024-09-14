# Simplyyy Tee: Hair & Beauty

This is a small web app for a local hairdresser to show their work and to gain more clients.

Users can navigate through the we app to view the hairstayles through the gallery and contact [Simplyyy Tee](https://www.instagram.com/simplyyytee/) directly or through her social media channels.

# Deployment via [Render.com](https://render.com)
You will need to `pip install gunicorn` and then make sure you have the libraries you have used in a `requirements.txt` file.  To do this, run the following commands in the terminal:
```
pip install gunicorn
pip freeze > requirements.txt
```

Now create a `Procfile   in your root directory.
```
web: gunicorn simplyTee:app
```
