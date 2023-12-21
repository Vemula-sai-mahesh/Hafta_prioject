from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
class Config(object):
    

    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/hafta'
    print("connected")
    # the biggest problem is that the database is created but we are not able to listen to the port
    # The next problem is that it seems the username and password are not being passed correctly
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']
    # LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # POSTS_PER_PAGE = 25
    
# Replace 'mysql://user:password@localhost/database' with your MySQL connection details
    db_url = 'mysql+pymysql://user:password@localhost/database'
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)  # Set echo to True for debugging (prints SQL statements)

    # Create a metadata instance
    metadata = MetaData()

    # Define the 'users' table
    users_table = Table(
        'users',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('age', Integer)
    )

    # Create the table in the database
    metadata.create_all(engine)

    # Perform database operations using the engine
    with engine.connect() as connection:
        # Example: Inserting a new user
        connection.execute(users_table.insert().values(name='Jane Doe', age=30))

        # Example: Querying users
        result = connection.execute(users_table.select())
        for row in result:
            print(f"User ID: {row['id']}, Name: {row['name']}, Age: {row['age']}")
