
# From Lucas

# "R _ _ L" -> "_ _ R L": TRUE
# "R _ _ L" -> "_ L _ R": FALSE
# "_ _ R _" -> "_ R _ _": FALSE
#
# "_ L R _" -> "L _ _ R": TRUE
#
# " LR L" -> " LR L"
#
# "_LR_L" -> "RL_L_": FALSE


# -----------------------------

def is_wrong_moved(str_initial, str_final):

    l_counter_initial = 0
    l_counter_final = 0
    r_counter_initial = 0
    r_counter_final = 0
    for i, char_initial in enumerate(str_initial):
        char_final = str_final[i]

        if char_initial == 'L':
            l_counter_initial += 1
        if char_final == 'L':
            l_counter_final += 1
        if l_counter_final < l_counter_initial:
            return False

        if char_initial == 'R':
            r_counter_initial += 1
        if char_final == 'R':
            r_counter_final += 1
        if r_counter_final > r_counter_initial:
            return False

    return True


arr_i = [ 'L___' , 'R___' , 'L___' , '_R__' , 'L_L_' , 'RR__', 'L__L', 'R__R', 'LR__', 'RL__', '__LR', '__RL', 'LLLR', 'RRRR', 'LLLL' ]
arr_f = [ 'L___' , 'R___' , '_L__' , 'R___' , 'LL__' , 'R_R_', 'LL__', '__RR', 'RL__', 'LR__', '__RL', '__LR', 'LLRL', 'RRRR', 'LLLL' ]
for str_initial, str_final in zip(arr_i, arr_f):

    print(str_initial, str_final)
    print(is_wrong_moved(str_initial, str_final))










