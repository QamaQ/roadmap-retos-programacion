# - Crea un comentario en el código y coloca la URL del sitio web oficial del
#     lenguaje de programación que has seleccionado.
# https://www.python.org/

# - Representa las diferentes sintaxis que existen de crear comentarios
#    en el lenguaje (en una línea, varias...).

# Comentario de Python
"""
Comentario de Python
"""
"Comentario de Python"

# - Crea una variable (y una constante si el lenguaje lo soporta).
variabl1 = 'var'
PI = 3.1416


# - Crea variables representando todos los tipos de datos primitivos
#    del lenguaje (cadenas de texto, enteros, booleanos...).
string = 'Hola Python', "Hola Python", """Hola Python"""
ints = 1,2,10,12
floats = 1.3,3.1416,12.e-3
booleans = True, False

print(f"""{
  string,
  ints,
  floats,
  booleans
  }""")

# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Python!")