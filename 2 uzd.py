def lasit_datni():
    pass
    try:
        saule=['augļus', 'dārzeņus','saldējumu']
        with open("teksts2.txt", 'w', encoding='utf8') as f:
            f.write('\n'.join(saule))
        saules=["","vaniļu saldējums","šokolādes saldējums "]
        with open('teksts2.txt', 'a', encoding='utf8') as dd:
                    dd.write('\n'.join(saules))
            
    except FileNotFoundError:
        print("datne nav atrasta!")
if __name__=="__main__":
  lasit_datni()