


import random



listaLogEmails = []
listaEmailDestino = []
emailEnvio = set()
emailDestino = set()



def ordenarEmailLongitud(email):
    return len(email)

def elegirEmailAleatorio(emailLista):
    numberRandom = random.randrange(0, len(emailLista))
    return numberRandom

def enviarEmail(email, emailEnvio):    
    for emailEnvio in sorted(emailEnvio, reverse=True):
        listaLogEmails.append(f"{emailEnvio} enviado a {email} [ok]\n")
        print(f"\n{emailEnvio} enviado a {email} [ok]", end="")
    return listaLogEmails

def escribirArchivo(listaEmails):
    escribirInfoEnvioEmail = open("Archivos/mensajes-consola.txt", "w")
    
    for i in range(len(listaEmails)):
        escribirInfoEnvioEmail.write(listaEmails[i])
    
    escribirInfoEnvioEmail.close()


# CREANDO LA ESTRUCTURA DEL PROGRAMA
fd = open("Archivos/mbox-short.txt", "r")

for line in fd:
    if line.startswith("From:"):
        emailDestino.add(line.split()[1])
fd.close()


direccionEmail = open("Archivos/mbox-short.txt", "r")

for linea in direccionEmail:
    if linea.startswith("To:"):
        emailEnvio.add(linea.split()[1])
direccionEmail.close()


# Imprimiendo los resultados
for emailDestino in sorted(emailDestino, reverse=False, key=ordenarEmailLongitud):
    listaEmailDestino.append(emailDestino)
    
while not len(listaEmailDestino) == 0:
    resultadoRandom = elegirEmailAleatorio(listaEmailDestino)
    email = listaEmailDestino.pop(resultadoRandom)
    logEmails = enviarEmail(email, emailEnvio)

escribirArchivo(logEmails)