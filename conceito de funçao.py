def saudar (nome):
    print (f"ola,{nome} !")
    
saudar(" ana ")
saudar ("bruno")
saudar ("carlos")
print("-"*30)

def estatisticas(nums):
    total = sum (nums)
    media = total / len (nums)
    return total, media

t,m = estatisticas ([8,9,7])
print(f"total : {t} , media : {m}")
print("-"*30)