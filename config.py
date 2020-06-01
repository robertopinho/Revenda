class config:
    #SQLALCHEMY_DATABASE_URI = 'mysql://robertoopinho:bancodedados@robertoopinho.mysql.pythonanywhere-services.com/robertoopinho$default'
    #SQLALCHEMY_DATABASE_URI = 'mysql:// USUARIO : SENHAMYSQL @robertoopinho.mysql.pythonanywhere-services.com/ BANCODEDADOS'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/revenda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT = "X#3jfk$%kKmGw&*jKLiPW@!jm345"
    JWT_SECRET_KEY = 'hjsdfhj#$@DFhsms@ldkPç()H#Dnx3@'
    JWT_BLACKLIST_ENABLED = True


