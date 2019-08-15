#ESCRIU EN UN HTML
#OBRE NAVEGADOR PER LLEGIR L'HTML ESCRIT UTILIZANT LA BIBLIOTECA WEBBROWSER

import webbrowser


ruta = "prueba.html"

with open(ruta, mode="w", encoding="utf-8") as fichero:
    print("<!DOCTYPE html>", file=fichero)
    print('<html lang="es">', file=fichero)
    print("<head>", file=fichero)
    print('  <meta charset="utf-8" />', file=fichero)
    print("  <title>HTML 5</title>", file=fichero)
    print('  <meta name="viewport" content="width=device-width, initial-scale=1.0" />', file=fichero)
    print("</head>", file=fichero)
    print("", file=fichero)
    print("<body>", file=fichero)
    print("  <p>hola</p>", file=fichero)
    print("</body>", file=fichero)
    print("</html>", file=fichero)


#obre utilitzant Navegador
webbrowser.open(ruta)

a