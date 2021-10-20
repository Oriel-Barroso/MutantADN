[![Coverage Status](https://coveralls.io/repos/github/Oriel-Barroso/Test/badge.svg?branch=master)](https://coveralls.io/github/Oriel-Barroso/Test?branch=master)

*Funcionamiento*

c_d_d, c_d_i, c_h --> Variables que me ayudan para el chequeo 
v_d_d --> Variable de salto utilizada para el slicing, sirve para la diagonal derecha
v_d_i --> Variable de salto utilizada para el slicing, sirve para la diagonal izquierda
v_v --> Variable de salto utilizada para el slicing, sirve para el chequeo vertical

No utilice para el chequeo de salto horizontal ya que siempre se suma de a uno

c_dd_s --> Variable de stop utilizada para el slicing, sirve para la diagonal derecha.
           El slicing va dando saltos hasta un valor indicado, entonces en el chequeo
           se va haciendo saltos hasta un determinado valor para capturar cuatro strings.
c_di_s --> Variable de stop utilizada para el slicing, sirve para la diagonal izquierda.
c_v_s --> Variable de stop utilizada para el slicing, sirve para el chequeo vertical
c_h_s --> Variable de stop utilizada para el slicing, sirve para el chequeo horizontal
val_diag_hor --> Variable que me evita hacer un chequeo diagonal derecho innecesario, 
                 tambien me sirve para el chequeo horizontal
val_if_no_diags_and_verticals --> Variable que me ayuda a no hacer un chequeo innecesario
                                  tanto para las diagonales como para la vertical. Es el
                                  que queda marcado con un numeral, apartir de ahi no hace
                                  mas comparaciones anteriormente dichas.
                                  Este valor siempre es el primero en la tercer fila 
                                  de abajo hacia arriba
                                  [----
                                   #---
                                   ----
                                   ----]
val_if_last_value_row --> Variable que me da el ultimo valor de la fila 1
total --> Variable que se incrementa a medida que va encontrando matches

lista[i:c_dd_s:v_d_d] == lista[i]*4, Aqui hacemos la comprobacion, gracias al slicing
                                     obtenemos 4 strings, luego comprobamos con la lista[i],
                                     aqui esta la primer letra del slicing, entonces multiplicandola
                                     por 4 obtenemos el string que estariamos buscando