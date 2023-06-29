from itsdangerous import URLSafeTimedSerializer as Serializer

def token(username,seconds):
    s=Serializer('*67@hjyjhk*',seconds)
    return s.dumps({'user':username}).decode('utf-8')
