print('Hola mundo')

nombre = input('Escribe tu nombre:')
apellido = input('Escribe tu apellido:')
edad = int(input('Escribe tu edad:'))
mail = input('Escribe tu mail:')

if nombre.strip() == '':
  print('El input no puede estar vacío')
else:
  print('El input es correcto, bien ahí')

if apellido.strip() == '':
  print('El input no puede estar vacío')
else:
  print('El input es correcto, bien ahí')

if edad <= 15:
  print('Niño/a')
elif edad >= 15 and edad <= 18:
  print('Adolescente')
elif edad >= 18:
  print('Adulto/a')

if mail.strip() == '':
  print('El input no puede estar vacío')
else:
  print('El input es correcto, bien ahí')

input(nombre)
input(apellido)
input(edad)
input(mail)

print(f'Hola {nombre.capitalize()} {apellido.capitalize()}, tenés {str(edad)} años y tu mail es el siguiente: {mail if '@' in mail else 'mail inválido'}')
