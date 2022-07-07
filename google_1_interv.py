
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

def count_l_by_R(str_tested):
    r_position = 0
    l_counter = 0

    arr_els_by_r = []
    arr_els = []
    for char in str_tested:
        if char == "L":
            arr_els.append([r_position, l_counter])
            l_counter += 1

        if char == "R":
            pair_R_L = [r_position, l_counter]
            arr_els_by_r.append(pair_R_L)

        r_position += 1

    return arr_els_by_r, arr_els


def is_crossed_LR(str_initial, str_final):

    arr_els_by_r_initial, arr_els_initial = count_l_by_R(str_initial)
    arr_els_by_r_final, arr_els_final = count_l_by_R(str_final)

    for i, pair_initial in enumerate(arr_els_by_r_initial):
        pair_final = arr_els_by_r_final[i]
        if pair_initial[1] < pair_final[1]:
            return True
        if pair_initial[0] > pair_final[0]:
            return True

    for i, pair_initial in enumerate(arr_els_initial):
        pair_final = arr_els_final[i]
        if pair_initial[1] > pair_final[1]:
            return True

    return False

str_initial = "L__R"
str_final = "L__R"

print(is_crossed_LR(str_initial, str_final))










