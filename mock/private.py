import datetime


def generate_url_endpoint():
    return str(int(datetime.datetime.now().timestamp()))
