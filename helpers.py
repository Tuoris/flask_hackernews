def get_app_host_and_port(app):
    server_name = app.config.get("SERVER_NAME")
    sn_host = sn_port = None

    if server_name:
        sn_host, _, sn_port = server_name.partition(":")

    if sn_host:
        host = sn_host
    else:
        host = "127.0.0.1"

    if sn_port:
        port = int(sn_port)
    else:
        port = 5000

    return (host, port)
