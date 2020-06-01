class config:
    SQLALCHEMY_DATABASE_URI = 'postgres://bwjylshfpgkhnm:314f4ef304df3c7c02b740f8d2e00bea6ab7e9eb8be12205bd48b28a60a9bb57@ec2-3-222-30-53.compute-1.amazonaws.com:5432/d8i554cdnpqkpc'
    #SQLALCHEMY_DATABASE_URI = 'mysql://robertoopinho:bancodedados@robertoopinho.mysql.pythonanywhere-services.com/robertoopinho$default'
    #SQLALCHEMY_DATABASE_URI = 'mysql:// USUARIO : SENHAMYSQL @robertoopinho.mysql.pythonanywhere-services.com/ BANCODEDADOS'

    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/revenda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT = "X#3jfk$%kKmGw&*jKLiPW@!jm345"
    JWT_SECRET_KEY = 'hjsdfhj#$@DFhsms@ldkPç()H#Dnx3@'
    JWT_BLACKLIST_ENABLED = True


