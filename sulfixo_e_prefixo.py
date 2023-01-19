input_user = input("digite seu alfabeto:")
pala_loc = input("letra a ser localizada:")

input_user = list(input_user)

one = input_user.index(pala_loc) -1
n = len(input_user) -1

valor_pre = []
valor_sul = []

if True:
    i = -1
    while i < one:
        i = i + 1
        val  = input_user[i]
        valor_pre.append(val)
        if i == one:
            break
if True:
    j = one + 1
    while j>= one:
        j = j + 1
        vol  = input_user[j]
        valor_sul.append(vol)
        if j == n:
            break

# print(valor_pre)
# print(valor_sul)
print(f"prefixo:{valor_pre}, sulfixo:{valor_sul}")
  
