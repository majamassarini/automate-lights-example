import pywebcopy

url = "http://172.31.10.243:8181"
kwargs = {'project_name': 'pages'}

payload = {'username': "admin", 'password': "admin"}
pywebcopy.SESSION.post("{}/login".format(url), data=payload)

pywebcopy.save_website(
    url=url,
    project_folder='.',
    **kwargs
)

