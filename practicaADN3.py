from time import time
import random


def check_automatizer(lista):
    A,T,C,G = 'AAAA', 'TTTT', 'CCCC', 'GGGG' 
    c_d_d, c_d_i, c_h = 0, 0, 0
    v_d_d = round(len(lista) ** 0.5) + 1
    v_d_i = v_d_d - 2
    v_v = v_d_d - 1
    v_h = 1
    c_dd_s = round((len(lista)**0.5)) * 4
    c_di_s = round((len(lista)**0.5)) * 3
    c_v_s = c_dd_s
    c_h_s = round(len(lista) ** 0.5)
    val_if = round((len(lista)**0.5)) - 3 #4
    val_if_no_diags_and_verticals = (round(len(lista)**0.5) - 3) * round(len(lista)**0.5) #7
    val_if_last_value_row = round(len(lista) ** 0.5) - 1 #4
    total = 0 #1
    for i in range(0, len(lista)): #n
        if c_d_d < val_if and i < val_if_no_diags_and_verticals and \
           lista[i:c_dd_s:v_d_d] == A or lista[i:c_dd_s:v_d_d] == T or lista[i:c_dd_s:v_d_d] == C or \
           lista[i:c_dd_s:v_d_d] == G:
                total += 1
        
        if c_d_i >= 3 and i < val_if_no_diags_and_verticals and \
           lista[i:c_di_s:v_d_i] == A or lista[i:c_di_s:v_d_i] == T or lista[i:c_di_s:v_d_i] == C or \
           lista[i:c_di_s:v_d_i] == G:
                total += 1

        if c_h < val_if and \
           lista[i:c_h_s:v_h] == A or lista[i:c_h_s:v_h] == T or lista[i:c_h_s:v_h] == C or \
           lista[i:c_h_s:v_h] == G:
            total += 1

        if i < val_if_no_diags_and_verticals and \
           lista[i:c_v_s:v_v] == A or lista[i:c_v_s:v_v] == T or lista[i:c_v_s:v_v] == C or \
           lista[i:c_v_s:v_v] == G:
            total += 1

        if c_h == val_if_last_value_row and c_d_d == val_if_last_value_row \
           and c_d_i == val_if_last_value_row:
            c_h = -1 #1
            c_d_d = -1
            c_d_i = -1
        
        c_dd_s +=1
        c_di_s += 1
        c_h_s += 1
        c_v_s += 1
        c_d_d += 1
        c_d_i += 1 
        c_h += 1
        if total >= 2:
            return (True, total)
    return (False, total)


def main():
    letras = ['TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'AGGTAGGGTTTCTCTCTTTATC',
              'AGGTAGGGTTTCTCTCTTTATC',
              'AGGTAGGGTTTCTCTCTTTATC',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'AGGTAGGGTTTCTCTCTTTATC',
              'AGGTAGGGTTTCTCTCTTTATC',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'AGGTAGGGTTTCTCTCTTTATC',
              'AGGTAGGGTTTCTCTCTTTATC',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'AGGTAGGGTTTCTCTCTTTATC',
              'AGGTAGGGTTTCTCTCTTTATC',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'TGTAGTATGTAGAGGTAGCCCT',
              'AGGTAGGGTTTCTCAAAAAAAA']
    lista = "".join(letras)
    print(len(lista))
    if len(lista) < 16:
        print('El largo de la lista debe ser mayor a 16')
    else:
        start_time = time()
        f = check_automatizer(lista)
        elapsed_time = time() - start_time
        print(f'En main {f} : ', elapsed_time)


if __name__ == '__main__':
    main()
    
