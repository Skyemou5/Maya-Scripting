import maya.cmds as cmds

sel = cmds.ls(sl=True)
my_string = 'L_Leg_######_Jnt'
char_list = list(my_string)
#zfill
num_of_chars = my_string.count('#')#returns # amount
string_parts = my_string.partition('#' * num_of_chars)
string_piece = my_string.find('#')
indx = (string_piece + num_of_chars)

hash_arr = []
end_of_hash = indx - 1

# fill array
for s in range(string_piece, end_of_hash, 1):
    hash = char_list.pop(i)
    hash_arr.extend(hash)

new_str = ''.join(char_list)
replace_num_str = '1'
replace_num_int = 1


if string_parts[1]:
    for s in sel:
        new_num = replace_num_str.zfill(num_of_chars)
        new_str = new_str.replace('#', new_num)
        replace_num_int += 1
        replace_num_str = str(replace_num_int)
        cmds.rename(new_str)
else:
    cmds.error('AHHHHHHHHHHHHHHHHH')

