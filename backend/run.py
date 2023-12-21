from app import create_app

app = create_app()


# there must be an issue with what port is being exposed in the yaml file and being redirected here
if __name__ == "__main__":
    app.run(port="8000" , debug=True)
